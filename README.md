# PyFeat-2.x: A Python-based Effective Feature Generation Tool from DNA, RNA, and Protein/Peptide Sequences

<!-- #### Author: X ABC, Y ABC, and Z ABC. -->

### Background / Motivation / Abstract / Gist:
In Bioinformatics research, we usually notice using the same biological sequences and even the same algorithms, but the performance varies greatly. Researchers unearth the riddle; it is merely the different feature representation process. Feature representation techniques drastically enhance performance. In addition, we firmly do believe rational feature representation techniques are a significant contribution to Algorithmic-Bioinformatics and Machine Learning in Biological Sciences research. The PyFeat–2.x s a comprehensive Deep Learning friendly Python-based tool for generating various numerical feature representation schemes from DNA, RNA, and protein primary structure sequences.

&nbsp;

### 1. How does it works? or, What is the primary goal of the package?
We incorporated a bunch of state-of-the-art feature groups for DNA, RNA, and protein sequence. `PyFeat-2.x` takes FASTA file (anyName.fasta, anyName.fa, anyName.txt) as an input with some parameters for a specific type of sequences; produces the features as NumPy array format (~.npy).

Feature Generate Process | Feature Merge Process|
|:----------------------:|:--------------------:|
|<img src="https://github.com/mrzResearchArena/PyFeat-2.x/blob/master/Figures/Feature-Generate.png" width="550" height="350" /> | <img src="https://github.com/mrzResearchArena/PyFeat-2.x/blob/master/Figures/Merge-Feature.png" width="550" height="350" />|

&nbsp;

### 2. Download Package
#### 2.1. Direct Download
We can directly [download](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/mrzResearchArena/PyFeat-2.x) by clicking the link.

> **Note:** The package will download in zip format `(.zip)` named `PyFeat-2.x-master.zip`.


#### 2.2. Clone a GitHub Repository (Optional)

Cloning a repository syncs it to our local machine (Example for Linux-based OS). After clone, we can add and edit files and then push and pull updates.
- Clone over HTTPS: `user@machine:~$ git clone https://github.com/mrzResearchArena/PyFeat-2.x.git `
- Clone over SSH: `user@machine:~$ git clone git@github.com:mrzResearchArena/PyFeat-2.x.git `

&nbsp;

> **Note-1:** If the clone was successful, a new sub-directory appears on our local drive. This directory has the same name (PyFeat-2.x) as the `GitHub` repository that we cloned.

> **Note-2:** We can run any Linux-based command from any valid location or path, but by default, a command generally runs from `/home/user/`.

> **Note-3:** `user` is the name of our computer but your computer name can be different (Example: `/home/bioinformatics/`).


&nbsp;


### 3. Required Python Packages:
```
- Install: python (version >= 3.6)
- Install: numpy (version >= 1.15.0)
```

&nbsp;

### Table 1: Details Parameters/Arguments for the Features Generation:
|   Long Argument|   Short Argument |    Variable Type     |   Default  | Choices            | Is it a feature? | Applicable | Argument Help |
|     :---       |    :---:              |  :---:               |  :---:     | :---:              | :---:   | :---:      |  ---:|
| --sequenceType | -seq                  | string               | -seq=PROT  | {DNA, dna, RNA, rna, PROT, prot}  |:x:|:no_entry:| Please use {DNA, dna} for DNA squences, {RNA, rna} for RNA squences, {PROT, prot} for protein/peptide squences. |
| --fasta        | -fa                   | string               |  -fa=samplePROT.fa | None | :x: |:no_entry:| Please enter the UNIX-like path. Example: -fa=/home/user/anyFASTA.fa |
| --terminusLength| -t                   | integer              | -t=50      | None | :x: |:no_entry:| The terminusLength 30 to 100  performed well. |
| --gGap         | -g                    | integer              | -g=5      | None | :x: |:no_entry:| The -g value is between 1 to 5 performed well. |
| --kTuple       | -k                    | integer              | -k=3      | None | :x: |:no_entry:| The -k value is between 1 to 3 performed well. |
| --FkMers | -fkmer          | integer |  -fkmer=0   | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --FgGaps11          | -fg11             | integer |  -fg11=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --FgGaps12          | -fg12             | integer |  -fg12=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --FgGaps21          | -fg21             | integer |  -fg21=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PgGaps11         | -pg11             | integer |  -pg11=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PgGaps12         | -pg12             | integer |  -pg12=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PgGaps21         | -pg21               | integer |  -pg21=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PkMers         | -pkmer               | integer |  -pkmer=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --binaryProfileFeature | -bpf     | integer |  -bpf=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --BLOSUM62       | -blosum62        | integer |  -blosum62=0    | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PAM250         | -pam250          | integer |  -pam250=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesP1           | -pcpP1            | integer |  -pcpP1=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesP2           | -pcpP2            | integer |  -pcpP2=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesP3           | -pcpP3            | integer |  -pcpP3=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesP4           | -pcpP4            | integer |  -pcpP4=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesP5           | -pcpP5            | integer |  -pcpP5=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesD1           | -pcpD1            | integer |  -pcpD1=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA </li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesD2           | -pcpD2            | integer |  -pcpD2=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA </li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalPropertiesR1           | -pcpR1            | integer |  -pcpR1=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] RNA </li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --BLASTn          | -blastn           | integer |  -blastn=0     | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --transitionTransversion   | -tt              | integer |  -tt=0    | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |

> **Note:** The `= sign` is the optional for parameter agument, but if you use the `= sign`, please make sure there will be no space besides the `= sign`. (To know more explanation, please see Table 2.)

> **Note:** We can use both long arguments and short arguments.

> **Note:** Helpful Tips: You can always use a short argument to reduce typing and time.

&nbsp;

### Table 2: How does the use parameter?

| Argument Segment   |     Is it a valid?      | Issue  |
|----------|:-------------:|------:|
| -seq=PROT |  :heavy_check_mark: | None |
| -seq = PROT |    :x:   |   Please trim the blank spaces on both sides of the `= sign`. |
| -seq PROT |  :heavy_check_mark: | None |
| -seq &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PROT |  :heavy_check_mark: | None; Yes, multi spaces are allowed. |

> **Note-1:** We can also use `--seqType` (long argument) instead of `-seq` (short argument/shortcut argument).

> **Note-2:** Helpful Tips: You can avoid `=` in arguments.

&nbsp;

### 3. Generate Feature:
#### Example-1:
- ##### Generate only the `Binary Profile Feature`
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -bpf 1   # default: -seq PROT.
```

- ##### Generate only the `Binary Profile Feature` with the 40 terminus length.
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -bpf 1 -t 40   # default: -t 50.
```

#### Example-2:
- ##### Generate only the `Position-wised g-Gaps & monoMono Style`
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -fg11 1 # default: -t 50 -g 5, -k 3.
```
- ##### Generate only the `Position-wised g-Gaps & monoMono Style` with 3-gaps and 4-mers.
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -fg11 1 -g 3 -k 4   # default: -t 30, -g 5, -k 3.
```

#### Example-3:
- ##### Generate only the `transversion`
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -tt 1 -seq DNA # default: -seq PROT.
```

#### Example-4:
- ##### Generate multiple dataset in a single command
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -bits 1 blosum62 1 pam250 1 g11 1
```

> **Note:** The PyFeat-2.x tool is able to generate multiple dataset with different parameters.

&nbsp;

### 4. Merge Feature:

#### Input Format:
```
user@machine:~$ python merge.py <anyFileName> <anyFileName.npy> <anyFileName.npy>
user@machine:~$ python merge.py <anyFileName> <anyFileName.npy> <anyFileName.npy> <anyFileName.npy>
```

#### Example-1:
- ##### Merge Two File
```
user@machine:~$ python merge.py merge fg11-16.npy fg11-32.npy
```

#### Example-2:
- ##### Merge Three File, or Merge Multiple File
```
user@machine:~$ python merge.py merge fg11-16.npy fg11-32.npy fg11-32.npy
```

> **Note:** The PyFeat-2.x tool is able to merge the multiple datasets.
