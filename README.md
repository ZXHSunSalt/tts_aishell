# tts_aishell
tts training based aishell dataset
# introduce
In this repository, it has finished the fucntion of generating the train data which includes the data-mel and data-spec.
The following work will be down in the next stage.
# notice
1. The form of csv must be id|content|content,no matter the character ','
2. 10G wav files will generating more than 100G data-mel and data-spec files, so it needs enought space to store train data.
3. The import package needs to be noticed. I program with other project,so it add the tacotron.packages. when you want to build a new project, it doesn't need it.
