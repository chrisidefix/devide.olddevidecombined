# Copyright (c) Charl P. Botha, TU Delft.
# All rights reserved.
# See COPYRIGHT for details.


# wxTreeListCtrl
# wx.TR_HIDE_ROOT

import DICOMBrowserFrame
reload(DICOMBrowserFrame)
import gdcm
from moduleBase import moduleBase
from moduleMixins import introspectModuleMixin
import moduleUtils
import os
import sys
import wx

class Study:
    def __init__(self):
        self.patient_name = None
        self.uid = None
        self.description = None
        self.date = None
        # maps from series_uid to Series instance
        self.series_dict = {}
        # total number of slices in complete study
        self.slices = 0

class Series:
    def __init__(self):
        self.series_uid = None
        self.series_description = None
        self.modality = None
        self.filenames = []
        # number of slices can deviate from number of filenames due to
        # multi-frame DICOM files
        self.slices = 0

class DICOMBrowser(introspectModuleMixin, moduleBase):
    def __init__(self, module_manager):
        moduleBase.__init__(self, module_manager)

        introspectModuleMixin.__init__(
            self,
            {'Module (self)' : self})

        self._view_frame = moduleUtils.instantiateModuleViewFrame(
            self, self._moduleManager, 
            DICOMBrowserFrame.DICOMBrowserFrame)

        self._bind_events()

        self.sync_module_logic_with_config()

        self.view()

    def close(self):
        self._view_frame.close()
        introspectModuleMixin.close(self)

    def get_input_descriptions(self):
        return ()

    def get_output_descriptions(self):
        return ()

    def set_input(self, idx, input_stream):
        pass

    def get_output(self, idx):
        pass

    def execute_module(self):
        pass

    def logic_to_config(self):
        pass

    def config_to_logic(self):
        pass

    def view(self):
        self._view_frame.Show()
        self._view_frame.Raise()

    def _bind_events(self):
        fp = self._view_frame.files_pane

        fp.ad_button.Bind(wx.EVT_BUTTON,
                self._handler_ad_button)

        fp.af_button.Bind(wx.EVT_BUTTON,
                self._handler_af_button)

        fp.scan_button.Bind(wx.EVT_BUTTON,
                self._handler_scan_button)

    def _fill_studies_listctrl(self, study_dict):
        """Given a study dictionary, fill out the complete studies
        ListCtrl.
        """

        lc = self._view_frame.studies_lc
        # clear the thing out
        lc.DeleteAllItems()

        sc = DICOMBrowserFrame.StudyColumns

        item_data_map = {}
        for study_uid, study in study_dict.items():
            # clean way of mapping from item to column?
            idx = lc.InsertStringItem(sys.maxint, study.patient_name)
            lc.SetStringItem(idx, sc.description, study.description)
            lc.SetStringItem(idx, sc.date, study.date)
            lc.SetStringItem(idx, sc.num_images, str(study.slices))
            lc.SetStringItem(
                    idx, sc.num_series, str(len(study.series_dict)))
          
            # SetItemData wants a long as argument, so we give it the
            # hash of the study_uid, which is unique
            h = hash(study_uid)
            lc.SetItemData(idx, h) 

            # for sorting we build up this item_data_map with the same
            # hash as key, and the all values occurring in the columns
            # as sortable values
            item_data_map[h] = (
                    study.patient_name,
                    study.description,
                    study.date,
                    study.slices,
                    len(study.series_dict))

            # assign the datamap to the ColumnSorterMixin
            lc.itemDataMap = item_data_map

        lc.auto_size_columns()

    def _handler_ad_button(self, event):

        dlg = wx.DirDialog(self._view_frame, 
            "Choose a directory to add:",
                          style=wx.DD_DEFAULT_STYLE
                           | wx.DD_DIR_MUST_EXIST
                           )

        if dlg.ShowModal() == wx.ID_OK:
            self._view_frame.files_pane.dirs_files_lb.Append(dlg.GetPath())

        dlg.Destroy()

    def _handler_af_button(self, event):

        dlg = wx.FileDialog(
                self._view_frame, message="Choose files to add:",
                defaultDir="", 
                defaultFile="",
                wildcard="All files (*.*)|*.*",
                style=wx.OPEN | wx.MULTIPLE
                )

        if dlg.ShowModal() == wx.ID_OK:
            for p in dlg.GetPaths():
                self._view_frame.files_pane.dirs_files_lb.Append(p)

        dlg.Destroy()

    def _handler_scan_button(self, event):
        paths = []
        lb = self._view_frame.files_pane.dirs_files_lb
        for i in range(lb.GetCount()):
            paths.append(lb.GetString(i))

        study_dict = self._scan(paths)

        self._fill_studies_listctrl(study_dict)



    def _helper_recursive_glob(self, paths):
        """Given a combined list of files and directories, return a
        combined list of sorted and unique fully-qualified filenames,
        consisting of the supplied filenames and a recursive search
        through all supplied directories.
        """

        # we'll use this to keep all filenames unique 
        files_dict = {}
        d = gdcm.Directory()

        for path in paths:
            if os.path.isdir(path):
                # we have to cast path to str (it's usually unicode)
                # else the gdcm wrappers error on "bad number of
                # arguments to overloaded function"
                d.Load(str(path), True)
                # fromkeys creates a new dictionary with GetFilenames
                # as keys; then update merges this dictionary with the
                # existing files_dict
                normed = [os.path.normpath(i) for i in d.GetFilenames()]
                files_dict.update(dict.fromkeys(normed, 1))

            elif os.path.isfile(path):
                files_dict[os.path.normpath(path)] = 1


        # now sort everything
        filenames = files_dict.keys()
        filenames.sort()

        return filenames


    def _scan(self, paths):
        """Given a list combining filenames and directories, search
        recursively to find all valid DICOM files.  Build
        dictionaries.
        """

        # UIDs are unique for their domains.  Patient ID for example
        # is not unique.
        # Instance UID (0008,0018)
        # Patient ID (0010,0020)
        # Study UID (0020,000D) - data with common procedural context
        # Study description (0008,1030)
        # Series UID (0020,000E)

        # see http://public.kitware.com/pipermail/igstk-developers/
        # 2006-March/000901.html for explanation w.r.t. number of
        # frames; for now we are going to assume that this refers to
        # the number of included slices (as is the case for the
        # Toshiba 320 slice for example)

        tag_to_symbol = {
                (0x0008, 0x0018) : 'instance_uid',
                (0x0010, 0x0010) : 'patient_name',
                (0x0010, 0x0020) : 'patient_id',
                (0x0020, 0x000d) : 'study_uid',
                (0x0008, 0x1030) : 'study_description',
                (0x0008, 0x0020) : 'study_date',
                (0x0020, 0x000e) : 'series_uid',
                (0x0008, 0x103e) : 'series_description',
                (0x0008, 0x0060) : 'modality', # fixed per series
                (0x0028, 0x0008) : 'number_of_frames',
                (0x0028, 0x0010) : 'rows',
                (0x0028, 0x0011) : 'columns'
                }

        # find list of unique and sorted filenames
        filenames = self._helper_recursive_glob(paths)

        s = gdcm.Scanner()
        # add the tags we want to the scanner
        for tag_tuple in tag_to_symbol:
            tag = gdcm.Tag(*tag_tuple)
            s.AddTag(tag)

        # d.GetFilenames simply returns a tuple with all
        # fully-qualified filenames that it finds.
        ret = s.Scan(filenames)
        if not ret:
            print "scanner failed"
            return

        # s now contains a Mapping (std::map) from filenames to stuff
        # calling s.GetMapping(full filename) returns a TagToValue
        # which we convert for our own use with a PythonTagToValue
        #pttv = gdcm.PythonTagToValue(mapping)

        # what i want:
        # a list of studies (indexed on study id): each study object
        # contains metadata we want to list per study, plus a list of
        # series belonging to that study.

        # maps from study_uid to instance of Study
        study_dict = {} 

        for f in filenames:
            mapping = s.GetMapping(f)

            # with this we can iterate through all tags for this file
            # let's store them all...
            file_tags = {}
            pttv = gdcm.PythonTagToValue(mapping)
            pttv.Start()
            while not pttv.IsAtEnd():
                tag = pttv.GetCurrentTag() # gdcm::Tag
                val = pttv.GetCurrentValue() # string

                symbol = tag_to_symbol[(tag.GetGroup(), tag.GetElement())]
                file_tags[symbol] = val

                pttv.Next()

            # take information from file_tags, stuff into all other
            # structures...

            # we need at least study and series UIDs to continue
            if not ('study_uid' in file_tags and \
                    'series_uid' in file_tags):
                continue
            
            study_uid = file_tags['study_uid']
            series_uid = file_tags['series_uid']
           
            # create a new study if it doesn't exist yet
            try:
                study = study_dict[study_uid]
            except KeyError:
                study = Study()
                study.study_uid = study_uid

                study.description = file_tags.get(
                        'study_description', '')
                study.date = file_tags.get(
                        'study_date', '')
                study.patient_name = file_tags.get(
                        'patient_name', '')

                study_dict[study_uid] = study

            try:
                series = study.series_dict[series_uid]
            except KeyError:
                series = Series()
                series.series_uid = series_uid
                # these should be the same over the whole series
                # fixme: could be that they don't exist (handle)
                series.series_description = \
                    file_tags['series_description']
                series.modality = file_tags['modality']

                study.series_dict[series_uid] = series

            series.filenames.append(f)

            
            try:
                number_of_frames = int(file_tags['number_of_frames'])
            except KeyError:
                # means number_of_frames wasn't found
                number_of_frames = 1

            series.slices = series.slices + number_of_frames
            study.slices = study.slices + number_of_frames

        return study_dict


        

