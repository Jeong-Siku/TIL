# TIL Day 02

>2023년 03월 12일 일요일

# Git 명령어

## Git 기본 명령어
### 1. `git init`
- 디렉토리를 Git로 관리한다는 명령어
- `.git`이라는 숨김폴더 생성,`(master)`라고 표기된다.
  
  ```bash
  1. `git init`을 두번 실행하지 않는다.
  2. 절대로 홈디렉토리에서 git init을 하지않는다.
  ```

### 2. `git status`
- 파일의 현재 상태를 알려주는 명령어

### 3. `git add`
- Git이 해당 파일을 추적할 수 있도록 만든다.
- `git add .` 또는 `git add 파일명`

### 4. `git commit`
- 파일의 변경사항을 하나의 버전(커밋)으로 저장하는 명령어
- `git commit -m ""`

### 5. `git log`
- 커밋의 내역을 조회
- 옵션
  - `-oneline`: 한 줄로 축약
  - `-graph`: 브랜치와 머지 내역을 그래프로 보여준다.
  - `-all`: 현재 브랜치를 포함한 모든 브랜치의 내역을 보여준다.
  - `reverse`: 커밋 내역의 순서를 반대로 보여준다.(최신이 가장 아래)
  - `p`: 파일의 변경 내용도 보여준다.
  - `2`: 원하는 갯수 만큼의 내역을 보여준다.

### 6. `git reset HEAD^~`
- `최근의 커밋 1개`를 지워준다.
- ~을 붙이고 숫자를 추가하면 개수만큼 삭제한다.

### 7. `git push -f`
- 원격 저장소에 커밋 기록을 `반영`
- 강제로 푸시하여 기록을 `삭제`
- -f를 사용해서 강제로 푸시하는 것은 `협업`시 `지양`할 것.



# Github
## 원격저장소
*(1) Github에서 원격 저장소 생성*  
*(2) 로컬저장소와 원격저장소 연결*

## 연결 명령어
### 1. git remote
- 등록: `git remote add <저장소 이름> <주소>` ex.이름 = origin
- 조회: `git remote remote -v`
- 삭제: `git remote rm <저장소 이름>`
## 업로드 명령어
### 1. git push
- 로컬 저장소의 커밋을 원격저장소에 업로드  
-`git push <저장소 이름> <브랜치이름>`   
  `-u`옵션을 사용하면, 두번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능
## 원격 저장소 가져오기

### clone,pull
1. git clone: 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
   - `git clone <원격 저장소 주소>`
   - `git init`과 `git remote add`가 이미 수행되어 있음
  
2. git pull: 원격 저장소의 변경 사항을 가져와서, 조컬 저장소를 업데이트하는 명령어
    - `git pull <저장소 이름> <브랜치 이름>`
  
## 과정
- `git pull → 문서저장 → git add → git commit → git push`

# .gitignore
>특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것
- `.gitignore` 파일은 `.git`폴더와 동일한 위치에 생성한다
- `git add` 전에 `.gitignore`에 작성한다.

- [.gitignore 쉽게 작성하기](https://www.toptal.com/developers/gitignore/)

# Branch
>Git에서 Branch라는 개념은 매우 중요하다. 사실상 버전관리의 꽃

## Branch 명령어
## 1. git branch
- 브랜치 조회, 생성, 삭제 등 명령어
```bash
- `-r` : 목록 확인
- 생성: `git branch <브랜치 이름>`
- 특정 커밋기준으로 생성: `git branch <브랜치 이름> <커밋 ID>`
- 삭제: `git branch -d <브랜치 이름>`
- `git branch -D <브랜치 이름>`
```
## 2. git switch
- 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어
```bash
이동: git switch <다른 브랜치 이름>
생성과 동시에 이동: git switch -c <브랜치 이름>
특정 커밋 기준으로 브랜치 생성과 동시에 이동: git switch -c <브랜치 이름> <커밋 ID>
```

# Branch Merge
>브랜치 작업이 끝난 뒤 작업내용을 master에 반영

## git merge
- `git merge <합칠 브랜치 이름>`
- Merge하기 전에, 메인 브랜치로 switch로 해야한다.

# Branch를 이용한 협업 방법
## 1. 원격 저장소 소유권이 있는 경우
- `clone` -> `git switch -c <작업할 브랜치>` -> `push` -> `git branch -d <작업한 브랜치>` -> `git switch master` -> `pull`
## 2. 원격 저장소 소유권이 없는 경우
- `fork`
- `clone` -> `remote add upsteram <주소>` -> `switch -c` -> `push` -> `branch -d` -> `switch` -> `pull`