#!/bin/bash

set -eu

mydir=$(cd $(dirname ${BASH_SOURCE:-$0});pwd)
git_dir=$(cd ${mydir}/..;pwd)

rpmbuild -bb --buildroot="${git_dir}/build/rpm/root" --eval="%define git_dir ${git_dir}" --eval="%define _topdir ${git_dir}/build/rpm" "${git_dir}/build/rpm/SPECS/ninjab.spec"

# Copy the created rpm to -latest
cp -f ${git_dir}/build/rpm/RPMS/noarch/$(ls ${git_dir}/build/rpm/RPMS/noarch/ | tail -n 1) ${git_dir}/build/rpm/RPMS/noarch/ninjab-latest.noarch.rpm

