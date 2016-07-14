#!/bin/sh

rm -rf /local/utilenv/bin
rm -rf /local/utilenv/include
rm -rf /local/utilenv/lib
rm -rf /local/utilenv/repo/links
rm -f /local/utilenv/install-log.txt

# Make sure paths/etc. are set up
. /etc/profile

cd /local/utilenv/repo
./make-index.pl

# Inherit from systemwide dir - for now
virtualenv --never-download --no-site-packages /local/utilenv
. /local/utilenv/bin/activate

grep -v "#" /local/utilenv/repo/pkgs-to-install.txt | while read pkg
do
    echo ""
    echo ""
    echo "+ easy_install -i file:///local/utilenv/repo/links -U $pkg"
    easy_install -i file:///local/utilenv/repo/links -U $pkg
    echo ""
done 2>&1 | tee -a /local/utilenv/install-log.txt

chown -R utility:utility /local/utilenv

# If utility already installed, run setup
if [ -e /local/utility/launch-admin-setup.sh ]; then
su utility -c "/local/utility/launch-admin-setup.sh"
fi
