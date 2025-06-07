"""requirements.txt 파일을 만들기 위한 모듈 불러오기"""
import subprocess
import os
import chardet

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')

# 인코딩 종류 알아보기
with open("requirements.txt", "rb") as f:
    info_result = chardet.detect(f.read(10000))  # 샘플로 10000바이트 분석
    print(info_result)

# version 긁어올 수 있는 함수 만들기

def get_version(package_name):
    """ 'pip show 패키지명'을 통해서 version을 긁어올 것 입니다. """
    try:      
        result = subprocess.run(
            ["pip", "show", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        for split_line in result.stdout.splitlines():
            if split_line.startswith("Version:"):
                return split_line.split(":")[1].strip()
    except Exception:
        return None


# pip freeze로 얻은 requirements.txt 불러오기
with open("requirements.txt", "r", encoding="UTF-16") as f:
    lines = f.readlines()

# 결과 확인
print(lines)

# 지저분한 형식을 '패키지==버전' 형식으로 바꾼 리스트 만들기
clean_lines=[]

for line in lines:
    if '@' in line:
        pn = line.split('@')[0].strip()
        v = get_version(pn)
        if v:
            clean_lines.append(f'{pn}=={v}\n')
        continue     # 만약 v==None인 경우 clean_lines에 넣지 말고 넘어감
    clean_lines.append(line)


with open("requirements.txt", "w", encoding="UTF-16") as f:
    f.writelines(clean_lines)


