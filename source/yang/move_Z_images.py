import pandas as pd
import os
import csv

# test
########################
#csv_filename = '/Users/tntjd5596/Downloads/ML_Patient monitor data/Z_RCM_AWRR_10.CSV'
#save_csv_filename = '/Users/tntjd5596/Downloads/ML_Patient monitor data/F_RCM_AWRR_10.CSV'
#original_image_dir = "/Users/tntjd5596/Downloads/ML_Patient monitor data/RCM/AWRR/10/"
#move_image_dir = '/Users/tntjd5596/Downloads/ML_Patient monitor data/RCM/AWRR/10_Z/'
#csv_label = 'label'

#######################


#입력부
##################################################
csv_dir = input("csv 디렉토리 : ")
csv_name = input("csv 파일 이름 : ")
save_csv_dir = input("Z를 제외한 csv를 새로 저장할 디렉토리 : ")
save_csv_name = input("새로 저장할 csv파일 이름 : ")

csv_lab = input("csv 라벨 (기본값:label) : ")

image_dir = input("기존 이미지 디렉토리 : ")
move_img_dir = input("이동할 이미지 디렉토리 : ")


################################################## 

# 최종 경로
csv_filename = csv_dir + "/" + csv_name
save_csv_filename = save_csv_dir + "/" + save_csv_name
csv_label  = csv_lab
original_image_dir = image_dir + "/"
move_image_dir = move_img_dir + "/"






csv_data = pd.read_csv(csv_filename , encoding='utf-8')
# csv_data를 읽어온다

j = 0
label=[]
index = 0
image_dir = os.listdir(original_image_dir)
# os명령어를 이용해 original_image_dir에 있는 파일명들을 리스트로 받아온다.

for i in csv_data[csv_label]:
    if(i=='Z'):
        print(index)
        csv_data[csv_label].pop(index)
        # csv_data에서 발견한 인덱스를 뽑아내고 삭제한다.
        os.rename(original_image_dir+'/'+image_dir[index],\
                  move_image_dir+ "/" +image_dir[index] ) 
        # os명령어를 이용해 Z가 있는 인덱스에 맞는 이미지를 다른 폴더로 이동시킨다.
        index += 1
        j += 1
    else:
        label.append(i[0])
        # Z가 아닌것들만 label리스트에 추가
        index += 1
else:
    print("How many moves? : ", j)

print("Complete")

f = open(save_csv_filename,'w')
# 새로운 csv파일 작성
for i in range(len(label)):
    csvWriter = csv.writer(f)
    csvWriter.writerow([label[i]])
    # Z가 아닌것들만 모아놓은 label리스트를 csv파일로 저장.
    
f.close()
