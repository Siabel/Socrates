
# Four Knights
👉 [GAME DOWNLOAD](https://www.4knights.co.kr/)</br>
👉 [GAME BUILD](https://drive.google.com/file/d/1qq7B22QTlkQIdM7Nag6u3Uq9VSMu39rh/view)</br> 
👉 [SOURCE CODE/ASSETS](https://drive.google.com/file/d/1jZvaquzq2abatI_Ial-WfpkSTaiy_QAx/view?usp=sharing/)</br>

## 목차
1. [개요](#Four-Knights)
2. [설계 문서](#설계-문서)
3. [개발 환경](#개발-환경)
4. [프로젝트 구조](#프로젝트-구조)
5. [팀원 소개](#팀원-소개)

## Four Knights
- 4가지의 직업 중 하나를 선택하여 사냥과 보스를 통해 재화를 얻고, 장비를 강화하며 성장하는 재미를 얻는다.
### 1.	사냥
- 솔로 플레이
- 핵 앤 슬래시
### 2.	레이드
- 멀티 플레이
- 1인 ~ 4인 파티 입장
### 3. 강화/승급
- 6개의 부위 강화 (투구, 갑옷, 장갑, 신발, 벨트, 무기)
- 10단계의 강화와 승급 시스템
### 4. 직업 4개
- 전사, 궁수, 마법사, 권사
### 5. 인게임
#### 1. 시작 화면 (서버 선택/캐릭터 선택)
<img src="./readme_img/01. 서버 선택.png" width="500">
<img src="./readme_img/02. 캐릭터 선택.png" width="500">

#### 2. 마을 (시작하는 마을/잡화상점/장비강화)
<img src="./readme_img/03. 마을.png" width="500">

<img src="./readme_img/06. 잡화상점.png" width="500">
<img src="./readme_img/07. 강화.png" width="500">

#### 3. 파티 (생성/찾기/참여/입장)
<img src="./readme_img/04-1. 파티 생성.png" width="500">
<img src="./readme_img/04-2. 파티 찾기.png" width="500">

<img src="./readme_img/04-3. 파티 참여.png" width="500">
<img src="./readme_img/04-4. 파티 입장.png" width="500">

#### 4. 보스 (골렘/드라이어드)
<img src="./readme_img/05-1. 골렘.png" width="500">
<img src="./readme_img/05-2. 드라이어드.png" width="500">

#### 5. 필드 (버려진 외곽/잃어버린 숲)
<img src="./readme_img/08. 사냥터.png" width="500">
<img src="./readme_img/08. 사냥터2.png" width="500">

#### 6. 사망
<img src="./readme_img/09. 사망.png" width="500">

#### 7. WEB
<img src="./readme_img/WEB.png" width="500">

#### 8. WPF
<img src="./readme_img/WPF1.png" width="280">
<img src="./readme_img/WPF2.png" width="250">

<img src="./readme_img/WPF3.png" width="500">

## 설계 문서
- [컨벤션](https://nettle-donkey-951.notion.site/Convention-71dbb58adf8d46b09c421e2cde5d4e90?pvs=4)
- [기능/요구사항 명세서](https://nettle-donkey-951.notion.site/dc010b83176b43778419526911acd1e9?pvs=4)
- [ERD](https://nettle-donkey-951.notion.site/ERD-acbacd0e561b4f95a49cd70aa2b59b90?pvs=4)
- [API](https://nettle-donkey-951.notion.site/API-b7975c3500b1483a8fca51dbefbd8315?pvs=4)


## 개발 환경

#### Front-end
![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white)<br/>

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/1.89.1-515151?style=for-the-badge)<br/>

#### Back-end


#### Database
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white)
![MySQL](https://img.shields.io/badge/8.0.36-515151?style=for-the-badge)<br/>

#### Web
![JS](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)<br/>
![React](https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=white)<br/>

#### Management Tool
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white)<br/>
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)<br/>
![Mattermost](https://img.shields.io/badge/Mattermost-0058CC?style=for-the-badge&logo=Mattermost&logoColor=white)<br/>

## 프로젝트 구조
### [Front-end]
```
└─B208
    ├── Assets
    │   ├── 01.Scenes
    │   ├── 02.Scripts
    │   ├── 03.Prefabs
    │   ├── 04.Audio
    │   ├── 05.Font
    │   ├── 06.Sprites
    │   ├── 07.Animation
    │   ├── ExternalAssets
    │   ├── Materials
    │   ├── Photon
    │   ├── Plugins
    │   ├── Polygon Arsenal
    │   ├── Resources
    │   ├── Samples
    │   ├── Settings
    │   └── TextMesh Pro  
    ├── Library
    ├── Logs
    ├── Packages
    ├── ProjectSettings
    └── UserSettings
```

### [Back-end]
```
└─knight
    ├─.gradle  
    ├─.idea
    ├─build
    ├─gradle
    └─src
        ├─main
        │  ├─java
        │  │  └─b208
        │  │      └─knight
        │  │          ├─api
        │  │          │  ├─controller
        │  │          │  ├─dto
        │  │          │  │  ├─request
        │  │          │  │  └─response
        │  │          │  └─service
        │  │          ├─common
        │  │          │  ├─config
        │  │          │  ├─exception
        │  │          │  └─model
        │  │          │      └─response
        │  │          └─db
        │  │              ├─entity
        │  │              ├─join
        │  │              └─repository
        │  └─resources
        │      ├─static
        │      ├─templates
        │      └─application.properties
        └─test
            └─java
                └─b208
                    └─knight
```

## 팀원 
### 소개
<img src = "./README_img/팀원소개.png" width=50%>

### 역할
#### 이은규 (팀장)

- 와이어 프레임 & UI 디자인 담당 <br>
  <img src = "./README_img/와이어프레임&UI디자인.png" width=30%>
- 발표 자료 제작

#### 정원종 (팀원)
