Name:        tui
Version:     0.6.3
Release:     27%{?dist}
Summary:     Text User Interface framework for scripts

License:     GPLv3
URL:         https://github.com/sri-arjuna/tui
#Source0:     https://github.com/sri-arjuna/tui/archive/master.zip
Source0:     http://sea.fedorapeople.org/review/%{name}/%{name}-%{version}.tar.gz

BuildArch:   noarch

Requires:    leafpad
Requires:    nano
Requires:    w3m
Requires:    coreutils
Requires:    wget
Requires:    xterm

%description
It is a framework of commands, to simply realize a basic
Text User Interface with their own scripts.
Besides 4(5) core commands, there are many other commands
which ease the task of writing a script.
Once you got use

Core Interface Commands:
* tui-echo (Prints up to 3 strings, newline)
* tui-header (Shows ForeGround color as font, and BG as BG)
* tui-printf (Prints up to 3 strings, stays_on_current_line)
* tui-title (Shows BG color as font, and FG color as BG)

Core Code helpers
* tui-bgjob (Executes script in the background,
             showing an animation while working...)
* tui-progress (Showing the next animation step per call)
* tui-read
* tui-status (Prints another message according to exit code) 
* tui-yesno (Returs TRUE on 'y', and FALSE on 'n')

Core Tools:
* tui-browser (Browsed given path as 'root')
* tui-conf-editor (Basic wizzard editor)
* tui-conf-get (Function as script)
* tui-conf-set (Function as script)
* tui-log (Helps you manage log file/s(-entries) and print to screen)
* tui-new-browser
* tui-new-script
* tui-psm (Paralell Script Manager)

The assistant commands are:
* tui-bol-dir
* tui-dd
* tui-download
* tui-edit
* tui-indi
* tui-install
* tui-list
* tui-press
* tui-str-usb
* tui-tar
* tui-terminal
* tui-wait
* tui-web

%prep
%setup -q -c %{name}-%{version}

%build
# nothing to do

%install
# Clean buildroot
rm -rf       %{buildroot}
# Remove non-used files to reduce package size
rm -fr  %{name}/build-rpm-%{name}.sh \
        %{name}/install.sh \
        %{name}/uninstall.sh
# Prepare directories
mkdir -p     %{buildroot}%{_bindir}/ \
                     %{buildroot}%{_mandir}/man1 \
                     %{buildroot}%{_sysconfdir}/%{name}/ \
                     %{buildroot}%{_sysconfdir}/profile.d/ \
                     %{buildroot}%{_datarootdir}/%{name}/themes \
                     %{buildroot}%{_docdir}/%{name} \
		     %{buildroot}%{_sysconfdir}/bash_completion.d/
# Move the executeables
rm -fr %{name}/screenshots
mv %{name}/bin/*     %{buildroot}%{_bindir}/
mv %{name}/%{name}_compl.bash %{buildroot}%{_sysconfdir}/bash_completion.d/
# Copy system defaults to system
cp %{name}/conf.etc/*    %{buildroot}%{_sysconfdir}/%{name}/
# Move system defaults to app dir
mv %{name}/conf.etc    %{buildroot}%{_datarootdir}/%{name}/
cp %{name}/conf.home/*  %{buildroot}%{_datarootdir}/%{name}/
mv %{name}/templates    %{buildroot}%{_datarootdir}/%{name}/
mv %{name}/themes       %{buildroot}%{_datarootdir}/%{name}/
mv %{name}/docs/*       %{buildroot}%{_docdir}/%{name}
mv %{name}/man/*.1      %{buildroot}%{_mandir}/man1

# Lets try once again without this...
rm -fr  %{name}/profile.d/tui.sh
#mv %{name}/profile.d/tui.sh	%{buildroot}%{_sysconfdir}/profile.d/tui.sh
# Keep for compatiblity
touch %{buildroot}%{_sysconfdir}/profile.d/tui.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)   
%doc %{_docdir}/%{name}/
%{_mandir}/man1/%{name}*.1.gz
%{_datarootdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/%{name}-*
#%{_sysconfdir}/%{name}/
#%{_sysconfdir}/profile.d/%{name}.sh

%config
%{_sysconfdir}/%{name}/
%{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/bash_completion.d/%{name}_compl.bash

%changelog
* Fri Dec 12 2014 - Simon A. Erat - erat.simon@gmail.com - 0.6.3-6
- Added: tui-new-manpage
- Fixed: tui-read
- Fixed: emptyline of tui-list/tui-select

* Thu Dec 11 2014 - Simon A. Erat - erat.simon@gmail.com - 0.6.3-0
- Updated: tui-list, roman numbering now uses CI) rather than M.
- Updated: tui-status, status.conf, uses now colors
- Added:   tui-filemgr
- Updated: tui-{edit,web}
- Updated: manpages of tui-{edit, filemgr, web, terminal}
- Added:   Bash completion

* Mon Dec 08 2014 - Simon A. Erat - erat.simon@gmail.com - 0.6.2-1
- Fixed:   tui-select now uses tui-list to print its options
- Updated: tui-list now supports roman numbers
- Updated: tui-select seems stable now, wrong input fills the line though...
- Updated: tui-conf-editor uses now tui-select
- Fixed:   tui-conf-editor applies supplied title
- Added:   demo & sample scripts, screenshots
- Performance update for tui-list

* Sun Dec 07 2014 - Simon A. Erat - erat.simon@gmail.com - 0.6.1-0
- Fixed: tui-conf-set, automaticly shell escapes when writing values
- Updated: tui-new-script, handling & templates
- Introducing: tui-select

* Mon Dec 01 2014 - Simon A. Erat - erat.simon@gmail.com - 0.6.0-0
- Helptext update in tui-bgjob, tui-log, tui-wait
- Added verbose: (-v) in: tui-{log, wait}
- Fixes in: tui, tui-{browser, conf-editor}

* Fri Nov 28 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.9-2
- Updated website in the manpages & prepared spec for 'tui reset'

* Fri Nov 28 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.9-1
- General manpage update and unifiquation.

* Thu Nov 27 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.9-0
- tui-browser 'fix' argument passing to sub scripts
- tui-read, properly uses theme now
- tui-download, requires less variables.

* Tue Nov 18 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.8-21
- Fixed: tui-edit, was very slow loading
- Fixed: tui-browser passes now arguments to scripts it executes

* Thu Nov 13 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.8-1
- Fixed: Showed $USER instead of whoami ($USER_NAME)

* Thu Nov 13 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.8-0
- Added: Colors and Borders are now changeable by a theme
- Renamed: tui-value-* to tui-conf-*
- Renamed: tui-config-editor to tui-conf-editor

* Thu Nov 13 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.7-0
- Fixed: tui-tar, compress 'indicator' was not properly shown
- Fixed: tui-read, now shows the border
- Fixed: tui-config-editor, had a check wrong formated
- Fixed: tui-printf, less split up aligments
- Fixed: tui-value-set, didnt change value but reported so
- Removed: tui-printf-optimized, no more things to apply

* Wed Nov 12 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.6-0
- 'tui' should be fixed again for first call
- changed manpage for 'tui'

* Wed Oct 29 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.5-1
- Changed: tui-psm, attempt to hide default output of scripts working on
- Readded: Some reqs for the spec - leafpad, nano, w3m, xterm

* Mon Oct 27 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.5-0
- Fixed: tui-browser, location display & passed path/file recognition

* Sun Oct 19 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.4-0
- Fixed: tui-browser, now passes passed arguments
- Updated %%description

* Sat Oct 18 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.3-0
- Added tui-psm (Paralell Script Manager)

* Thu Sep 04 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.1-0
- Changed: colors.conf
- Changed: status.conf
- Fixing ATM: colors spread over lines

* Sun Aug 31 2014 - Simon A. Erat - erat.simon@gmail.com - 0.5.0-0
- Rewrote for performance
- Added tui-browser, tui-new-browser
- Added tui-install, tui-wait

* Thu Mar 20 2014 - Simon A. Erat - erat.simon@gmail.com - 0.4.1-0
- Introducing $USER_SHELL, used for tui-newscript as shell definition

* Sun Feb 02 2014 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-7
- Added:     tui.spec to package location
- Changed:   install.sh
- Changed:   tui-newscript.sh

* Sat Oct 26 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-6
- Added:     tui-bgjob

* Sun Oct 13 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-5
- Changed:   Optimized dd, download, tar

* Thu Oct 03 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-4
- Added:     tui-dd
- Changed:   Tarball now more structured

* Thu Oct 03 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-3
- Changed:   Renamed tui-str-ask -> tui-read
- Long line fix : attemp 1

* Mon Sep 30 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-2
- Changed:   Renamed 'global' variable DEFAULT_USER -> USER_NAME
- Changed:   Renamed 'global' variable DEFAULT_EMAIL -> USER_EMAIL
- Changed:   Renamed 'global' variable USER_HOMEPAGE -> USER_HOMEPAGE

* Sun Sep 29 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-1
- Added:     tui-tar
- Changed:   tui-download - Now displays amount of data downloaded

* Sat Sep 28 2013 - Simon A. Erat - erat.simon@gmail.com - 0.4.0-0
- Fixed:     Alignments & stable
- Spec:      Clean up

* Thu Sep 26 2013 - Simon A. Erat - erat.simon@gmail.com - 0.3.8-2
- Added:     tui-download, tui-str-ask, tui-str-usb
- Changed:   tui-newscript 
-            Rearanged argument handling after sourcing 'tui'
- Fixed:     ?tui-indi, missed variable check for proper tempdir
- Fixed:     tui-printf: Contained accidently \n instead or \r
- Spec:      Updated descripton

* Tue Sep 24 2013 - Simon A. Erat - erat.simon@gmail.com - 0.3.8-1
- Fixed:     Alignments - header/title (GUI still needs care)

* Tue Sep 24 2013 - Simon A. Erat - erat.simon@gmail.com - 0.3.8-0
- Updated:   Manpages
- Fixed:     Several files

* Sat Sep 21 2013 - Simon A. Erat - erat.simon@gmail.com - 0.3.7-2
- Added:     tui-status, tui-edit, tui-yesno, tui-press

* Sat Sep 21 2013 - Simon A. Erat - erat.simon@gmail.com - 0.3.7-1
- Fixed:     Display issues

* Sat Sep 21 2013 - Simon A. Erat - erat.simon@gmail.com - 0.3.7-0
- Initial package, providing: tui, tui-printf, tui-echo, 
-                             tui-header, tui-title, tui-newscript
- 'High' version number because it is the "framework" i was using
- for Script-Tools, extracted and (in process to) polished up for reusage
