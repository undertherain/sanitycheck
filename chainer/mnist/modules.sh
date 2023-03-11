# System

function set_env 
{
    if [ -d "$1/bin" ]; then
        export PATH=$1/bin:$PATH
    fi
    if [ -d "$1/bin/intel64" ]; then
        export PATH=$1/bin/intel64:$PATH
    fi
    if [ -d "$1/bin64" ]; then
        export PATH=$1/bin64:$PATH
    fi
    if [ -d "$1/lib" ]; then
        export LD_LIBRARY_PATH=$1/lib:$LD_LIBRARY_PATH
        export LIBRARY_PATH=$1/lib:$LIBRARY_PATH
    fi
    if [ -d "$1/lib/intel64" ]; then
        export LD_LIBRARY_PATH=$1/lib/intel64:$LD_LIBRARY_PATH
        export LIBRARY_PATH=$1/lib/intel64:$LIBRARY_PATH
    fi
    if [ -d "$1/lib64" ]; then
    export LD_LIBRARY_PATH=$1/lib64:$LD_LIBRARY_PATH
        export LIBRARY_PATH=$1/lib64:$LIBRARY_PATH
    fi
#    if [ -d "$1/lib64/stubs" ]; then
#        export LD_LIBRARY_PATH=$1/lib64/stubs:$LD_LIBRARY_PATH
#        export LIBRARY_PATH=$1/lib64/stubs:$LIBRARY_PATH
#    fi
    if [ -d "$1/include" ]; then
        export C_INCLUDE_PATH=$1/include:$C_INCLUDE_PATH
        export CPLUS_INCLUDE_PATH=$1/include:$CPLUS_INCLUDE_PATH
    fi
    if [ -d "$1/man" ]; then
        export MAN_PATH=$1/man:$MAN_PATH
    fi
}


export PKG_CONFIG_PATH=/home/1/drozd-a-aa/opt/lib/pkgconfig
set_env /home/1/drozd-a-aa/opt
set_env /home/1/drozd-a-aa/opt/extra/gcc-5.4.0
set_env /usr/local/cuda-8.0/targets/x86_64-linux

. /etc/profile.d/modules.sh
module load cuda/8.0.61
module load nccl/2.1
module load cudnn/7.0
module load openmpi/2.1.2

# pyenv
# export PYENV_ROOT=${HOME}/.pyenv
# export PATH=${PYENV_ROOT}/bin:${PATH}
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"
