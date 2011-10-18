# next steps: 
# * is there a method that gets called for ALL attribute
#   access, also attributes that do exist in the dictionary?
# * what's up with the ModuleType?  modifying it's dict modifies also
#   the vtk dict.

import sys
import types

import vtk

class CVTK:
    def __init__(self):
        # why does dir(cvtk) at this moment give all the VTK
        # symbols??!  why are my mods on this __dict__ applied to VTK
        # itself?! -- that's because we were ModuleType
        for k,v in vtk.__dict__.items():
            if k.startswith('vtk'):
                # chop off the vtk
                new_k = k[3:]

                try:
                    # remove the current version
                    del self.__dict__[k]
                except KeyError:
                    pass

                self.__dict__[new_k] = None

            else:
                self.__dict__[k] = v

        # now let's go through all the VTK attributes and store them
        # in our own dictionary.  This is for completion type of stuff
        # to work.
        

    def __getattr__(self, attr):
        print "getattr"
        # __getattr__ only gets called if the attribute does not exist
        # it looks like __getattribute__ always gets called, but only
        # if we are a moduletype.  is there a method that gets called
        # for a normal class for ALL attribute access?
        try:
            vtk_class = getattr(vtk, 'vtk%s' % (attr,))
        except AttributeError:
            return getattr(vtk, attr)

        # create metaclass inline
        class VTKType(type):
            def __call__(cls, *args, **kwargs):
                print kwargs
                return vtk_class()

        class VTKClass:
            __metaclass__ = VTKType

        return VTKClass

    def test(self):
        print "hello!"


cvtk = CVTK()

