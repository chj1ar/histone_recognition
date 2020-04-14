
## Requirements

- pandas
- skbio
- rdkit
- tqdm
- csv

(test with Python 3.8.1)

**skbio install**
(enter conda venv)

[optional: faster pip source](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```bash
pip install scikit-bio
```

<details>
	<summary>test details</summary>

```bash
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting scikit-bio
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/66/b0/054ef21e024d24422882958072973cd192b492e004a3ce4e9614ef173d9b/scikit-bio-0.5.6.tar.gz (8.4 MB)
     |████████████████████████████████| 8.4 MB 116 kB/s
Collecting lockfile>=0.10.2
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/c8/22/9460e311f340cb62d26a38c419b1381b8593b0bb6b5d1f056938b086d362/lockfile-0.12.2-py2.py3-none-any.whl (13 kB)
Collecting CacheControl>=0.11.5
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/18/71/0a9df4206a5dc5ae7609c41efddab2270a2c1ff61d39de7591dc7302ef89/CacheControl-0.12.6-py2.py3-none-any.whl (19 kB)
Requirement already satisfied: decorator>=3.4.2 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (4.4.1)
Requirement already satisfied: IPython>=3.2.0 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (7.12.0)
Requirement already satisfied: matplotlib>=1.4.3 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (3.1.3)
Collecting natsort>=4.0.3
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/0f/65/81883897f4aaa1e53deaa65137318cfe80b36ce013c2e86f8fd0843cfa02/natsort-7.0.1-py3-none-any.whl (33 kB)
Requirement already satisfied: numpy>=1.9.2 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (1.18.1)
Requirement already satisfied: pandas>=1.0.0 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (1.0.1)
Requirement already satisfied: scipy>=1.3.0 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (1.4.1)
Collecting hdmedians>=0.13
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/df/19/b8c304859fa12a71eeadd2e90a7f19000c3f1281be370f035a9fce3b014f/hdmedians-0.13.tar.gz (3.1 kB)
Requirement already satisfied: scikit-learn>=0.19.1 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-bio) (0.22.2.post1)
Requirement already satisfied: requests in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from CacheControl>=0.11.5->scikit-bio) (2.22.0)
Collecting msgpack>=0.5.2
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/aa/48/be5864c5c3604c07edf2eebaaacb1bb9afe600abc85295ffddb39f5ab529/msgpack-1.0.0-cp38-cp38-macosx_10_13_x86_64.whl (78 kB)
     |████████████████████████████████| 78 kB 2.3 MB/s
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (3.0.3)
Requirement already satisfied: appnope; sys_platform == "darwin" in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (0.1.0)
Requirement already satisfied: pexpect; sys_platform != "win32" in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (4.8.0)
Requirement already satisfied: traitlets>=4.2 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (4.3.3)
Requirement already satisfied: jedi>=0.10 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (0.16.0)
Requirement already satisfied: backcall in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (0.1.0)
Requirement already satisfied: setuptools>=18.5 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (45.1.0.post20200127)
Requirement already satisfied: pickleshare in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (0.7.5)
Requirement already satisfied: pygments in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from IPython>=3.2.0->scikit-bio) (2.5.2)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from matplotlib>=1.4.3->scikit-bio) (2.4.6)
Requirement already satisfied: cycler>=0.10 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from matplotlib>=1.4.3->scikit-bio) (0.10.0)
Requirement already satisfied: python-dateutil>=2.1 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from matplotlib>=1.4.3->scikit-bio) (2.8.1)
Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from matplotlib>=1.4.3->scikit-bio) (1.1.0)
Requirement already satisfied: pytz>=2017.2 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from pandas>=1.0.0->scikit-bio) (2019.3)
Requirement already satisfied: Cython>=0.23 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from hdmedians>=0.13->scikit-bio) (0.29.16)
Requirement already satisfied: joblib>=0.11 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from scikit-learn>=0.19.1->scikit-bio) (0.14.1)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from requests->CacheControl>=0.11.5->scikit-bio) (1.25.8)
Requirement already satisfied: idna<2.9,>=2.5 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from requests->CacheControl>=0.11.5->scikit-bio) (2.8)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from requests->CacheControl>=0.11.5->scikit-bio) (2019.11.28)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from requests->CacheControl>=0.11.5->scikit-bio) (3.0.4)
Requirement already satisfied: wcwidth in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->IPython>=3.2.0->scikit-bio) (0.1.8)
Requirement already satisfied: ptyprocess>=0.5 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from pexpect; sys_platform != "win32"->IPython>=3.2.0->scikit-bio) (0.6.0)
Requirement already satisfied: ipython-genutils in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from traitlets>=4.2->IPython>=3.2.0->scikit-bio) (0.2.0)
Requirement already satisfied: six in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from traitlets>=4.2->IPython>=3.2.0->scikit-bio) (1.14.0)
Requirement already satisfied: parso>=0.5.2 in /usr/local/Caskroom/miniconda/base/envs/py3/lib/python3.8/site-packages (from jedi>=0.10->IPython>=3.2.0->scikit-bio) (0.6.1)
Building wheels for collected packages: scikit-bio, hdmedians
  Building wheel for scikit-bio (setup.py) ... done
  Created wheel for scikit-bio: filename=scikit_bio-0.5.6-cp38-cp38-macosx_10_9_x86_64.whl size=1042794 sha256=7eaeeffabcfca9a2b571775336a34145f29297d47be2251b3b3f6abd767c0e70
  Stored in directory: /Users/zrt/Library/Caches/pip/wheels/3a/f8/82/3eb5de2b7104f40f36b12583af6d3d676367897c2b160fb943
  Building wheel for hdmedians (setup.py) ... done
  Created wheel for hdmedians: filename=hdmedians-0.13-cp38-cp38-macosx_10_9_x86_64.whl size=150737 sha256=5b4d5c4acd11e95cc76c0c15969192d9e98b3eccd710862bb4ec415d4e54b8c0
  Stored in directory: /Users/zrt/Library/Caches/pip/wheels/43/61/17/8de21c181a8367ffa1ecd6060081aaf226057a5b443d5f78bc
Successfully built scikit-bio hdmedians
Installing collected packages: lockfile, msgpack, CacheControl, natsort, hdmedians, scikit-bio
Successfully installed CacheControl-0.12.6 hdmedians-0.13 lockfile-0.12.2 msgpack-1.0.0 natsort-7.0.1 scikit-bio-0.5.6
```
</details>


**rdkit install**
(enter conda venv)

[optional: faster conda mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

```bash
conda install -c conda-forge rdkit
```

<details>
	<summary>test details</summary>

```bash
(py3) ╭─zrt@zrtdeMacBook-Pro ~/code/histone_recognition ‹master*›
╰─$ conda install -c conda-forge rdkit
Collecting package metadata (current_repodata.json): done
Solving environment: |
Warning: >10 possible package resolutions (only showing differing packages):
  - https://repo.anaconda.com/pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0, https://repo.anaconda.com/pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  - defaults::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0, https://repo.anaconda.com/pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  - defaults::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0, https://repo.anaconda.com/pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  - defaults::libcxxabi-4.0.1-hcfea43d_1, defaults::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0, https://repo.anaconda.com/pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  - defaults::libedit-3.1.20181209-hb402a30_0, defaults::tk-8.6.8-ha441bb4_0, https://repo.anaconda.com/pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0
  - defaults::libcxxabi-4.0.1-hcfea43d_1, defaults::libedit-3.1.20181209-hb402a30_0, defaults::tk-8.6.8-ha441bb4_0, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0
  - defaults::tk-8.6.8-ha441bb4_0, https://repo.anaconda.com/pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0
  - defaults::libcxxabi-4.0.1-hcfea43d_1, defaults::tk-8.6.8-ha441bb4_0, https://repo.anaconda.com/pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::pip-20.0.2-py38_0
  - defaults::pip-20.0.2-py38_0, defaults::tk-8.6.8-ha441bb4_0, https://repo.anaconda.com/pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0
  - defaults::pip-20.0.2-py38_0, https://repo.anaconda.com/pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1, https://repo.anaconda.com/pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0, https://repo.anaconda.com/pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  ... and othedone


==> WARNING: A newer version of conda exists. <==
  current version: 4.7.12
  latest version: 4.8.3

Please update conda by running

    $ conda update -n base conda



## Package Plan ##

  environment location: /usr/local/Caskroom/miniconda/base/envs/py3

  added / updated specs:
    - rdkit


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    icu-64.2                   |       h6de7cb9_1        12.3 MB  conda-forge
    pandas-1.0.3               |   py38h5fc983b_0        10.3 MB  conda-forge
    pillow-7.0.0               |   py38h4655f20_0         568 KB  defaults
    six-1.14.0                 |             py_1          13 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        23.2 MB

The following NEW packages will be INSTALLED:

  boost              conda-forge/osx-64::boost-1.72.0-py38hbf1eeb5_0
  boost-cpp          conda-forge/osx-64::boost-cpp-1.72.0-hdf9ef73_0
  bzip2              conda-forge/osx-64::bzip2-1.0.8-h0b31af3_2
  cairo              conda-forge/osx-64::cairo-1.16.0-hec6a9b0_1003
  fontconfig         conda-forge/osx-64::fontconfig-2.13.1-h6b1039f_1001
  freetype           conda-forge/osx-64::freetype-2.10.1-h8da9a1a_0
  gettext            conda-forge/osx-64::gettext-0.19.8.1-h46ab8bc_1002
  glib               conda-forge/osx-64::glib-2.58.3-py38h338c551_1004
  icu                conda-forge/osx-64::icu-64.2-h6de7cb9_1
  jpeg               conda-forge/osx-64::jpeg-9c-h1de35cc_1001
  libblas            conda-forge/osx-64::libblas-3.8.0-16_openblas
  libcblas           conda-forge/osx-64::libcblas-3.8.0-16_openblas
  libgfortran        conda-forge/osx-64::libgfortran-4.0.0-2
  libiconv           conda-forge/osx-64::libiconv-1.15-h0b31af3_1006
  liblapack          conda-forge/osx-64::liblapack-3.8.0-16_openblas
  libopenblas        conda-forge/osx-64::libopenblas-0.3.9-h3d69b6c_0
  libpng             conda-forge/osx-64::libpng-1.6.37-hbbe82c9_1
  libtiff            conda-forge/osx-64::libtiff-4.1.0-h2ae36a8_6
  libwebp-base       conda-forge/osx-64::libwebp-base-1.1.0-h0b31af3_3
  libxml2            conda-forge/osx-64::libxml2-2.9.10-h53d96d6_0
  llvm-openmp        conda-forge/osx-64::llvm-openmp-10.0.0-h28b9765_0
  lz4-c              conda-forge/osx-64::lz4-c-1.8.3-h6de7cb9_1001
  numpy              conda-forge/osx-64::numpy-1.18.1-py38h1f821a2_1
  olefile            conda-forge/noarch::olefile-0.46-py_0
  pandas             conda-forge/osx-64::pandas-1.0.3-py38h5fc983b_0
  pcre               conda-forge/osx-64::pcre-8.44-h4a8c4bd_0
  pillow             pkgs/main/osx-64::pillow-7.0.0-py38h4655f20_0
  pixman             conda-forge/osx-64::pixman-0.38.0-h01d97ff_1003
  pycairo            conda-forge/osx-64::pycairo-1.19.1-py38hfdb331f_3
  python-dateutil    conda-forge/noarch::python-dateutil-2.8.1-py_0
  python_abi         conda-forge/osx-64::python_abi-3.8-1_cp38
  pytz               conda-forge/noarch::pytz-2019.3-py_0
  rdkit              conda-forge/osx-64::rdkit-2020.03.1-py38h415f5aa_1
  six                conda-forge/noarch::six-1.14.0-py_1
  zstd               conda-forge/osx-64::zstd-1.4.4-hed8d7c8_2

The following packages will be UPDATED:

  ca-certificates    pkgs/main::ca-certificates-2019.11.27~ --> conda-forge::ca-certificates-2020.4.5.1-hecc5488_0
  certifi              pkgs/main::certifi-2019.11.28-py38_0 --> conda-forge::certifi-2020.4.5.1-py38h32f6830_0
  libcxx                 pkgs/main::libcxx-4.0.1-hcfea43d_1 --> conda-forge::libcxx-10.0.0-0
  openssl              pkgs/main::openssl-1.1.1d-h1de35cc_3 --> conda-forge::openssl-1.1.1f-h0b31af3_0


Proceed ([y]/n)?


Downloading and Extracting Packages
pandas-1.0.3         | 10.3 MB   | ############################################################################################################################### | 100%
pillow-7.0.0         | 568 KB    | ############################################################################################################################### | 100%
six-1.14.0           | 13 KB     | ############################################################################################################################### | 100%
icu-64.2             | 12.3 MB   | ############################################################################################################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

</details>

Then, you can run similarity/calc_similarity.ipynb

