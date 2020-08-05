# PyFeat-2.x

PyFeat–2.x is an extensive Python-based tool for generating various numerical feature representation schemes from DNA, RNA, and protein primary structure sequences.

&nbsp;

##### x. Required Python Packages:
```
- Install: python (version >= 3.6)
- Install: numpy (version >= 1.15.0)
```

##### Table 1: Details Parameters/Arguments for the Features Generation
|   Argument     |   Argument (Shortcut) |    Variable Type     |   Default  | Choices              | Help   |
|     :---       |    :---:              |  :---:               |  :---:     | :---:                |    ---:|
| --seqType      | -seq                  | string               | -seq=PROT  | None  |Please use either DNA, RNA, or PROTEIN (PROT). |
| --fasta        | -fa                   | string               |  None      | None | Please enter the UNIX-like path. Example: -fa=/home/user/anyFASTA.fa |
| --gGap         | -g                    | integer              | -g=5      | None | The gap between 1 to 5 performed well. Example: -g=5  |
| --kTuple       | -k                    | integer              | -k=3      | None | The k between 1 to 3 performed well. Example: -k=3  |
| --pseudoComposition | -pseudo          | integer |  -pseudo=0   | {1, 0} | 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --monoMono          | -f11             | integer |  -f11=0      | {1, 0} | 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --monoDi            | -f12             | integer |  -f12=0      | {1, 0} | 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --diMono            | -f21             | integer |  -f13=0      | {1, 0} | 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |


&nbsp;
&nbsp;
&nbsp;


##### x. Generate Feature:
``` console
user@machine:~$ python main.py -fa acp500.txt -bpf 1
```
