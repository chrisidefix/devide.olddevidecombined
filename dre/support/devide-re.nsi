; devide.nsi - based on example2.nsi
; $Id: devide.nsi 2759 2008-02-23 20:56:40Z cpbotha $

;--------------------------------

; The name of the installer
Name "DeVIDE-RE"

; The file to write
OutFile "devide-re-setup.exe"

; The default installation directory
InstallDir $PROGRAMFILES\DeVIDE-RE

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM SOFTWARE\DeVIDE-RE "Install_Dir"

; The text to prompt the user to enter a directory
ComponentText "Select optional components."

; The text to prompt the user to enter a directory
DirText "Choose the directory where you'd like to install DeVIDE:"

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "DeVIDE-RE (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; take all these files (recursively yay)
  File /r "devide-re\*.*"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\DeVIDE-RE "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DeVIDE-RE" "DisplayName" "DeVIDE-RE (remove only)"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DeVIDE-RE" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteUninstaller "uninstall.exe"
  
SectionEnd

; optional section (can be disabled by the user)
Section "Start Menu Shortcuts"
  CreateDirectory "$SMPROGRAMS\DeVIDE-RE"

  CreateShortCut "$SMPROGRAMS\DeVIDE\DeVIDE.lnk" \
  "$INSTDIR\dre.cmd" "devide" \
  "$INSTDIR\devide\resources\graphics\devidelogo64x64.ico" 0

  CreateShortCut "$SMPROGRAMS\DeVIDE\DeVIDE no-itk.lnk" \
  "$INSTDIR\dre.cmd" "devide --no-kits itk_kit" \
  "$INSTDIR\devide\resources\graphics\devidelogo64x64.ico" 0

  CreateShortCut "$SMPROGRAMS\DeVIDE\Uninstall.lnk" \
  "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0  

SectionEnd

Section "Desktop Shortcut"
   CreateShortCut "$DESKTOP\DeVIDE.lnk" \
   "$INSTDIR\dre.cmd" "devide" \
   "$INSTDIR\devide\resources\graphics\devidelogo64x64.ico" 0

   CreateShortCut "$DESKTOP\DeVIDE no-itk.lnk" \
   "$INSTDIR\dre.cmd" "devide --no-kits itk_kit" \
   "$INSTDIR\devide\resources\graphics\devidelogo64x64.ico" 0

SectionEnd

;--------------------------------

; Uninstaller

UninstallText "This will uninstall DeVIDE. Hit next to continue."

; Uninstall section

Section "Uninstall"
  
  ; remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DeVIDE"
  DeleteRegKey HKLM SOFTWARE\DeVIDE

  ; remove files and uninstaller
  Delete $INSTDIR\*.*

  ; remove shortcuts, if any
  Delete "$SMPROGRAMS\DeVIDE\*.*"

  ; remove desktop shortcut
  Delete "$DESKTOP\DeVIDE.lnk"
  Delete "$DESKTOP\DeVIDE no-itk.lnk"

  ; remove directories used
  RMDir "$SMPROGRAMS\DeVIDE"

  ; actually this will do a recursive delete on everything
  RMDir /R "$INSTDIR"

SectionEnd



