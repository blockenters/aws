# aws

---

## 프로젝트 주제 

### 현대에서 정해준 큰 주제 : AWS 기반 서비스 보안 구축 프로젝트

#### 프로젝트 예시 ####

1. 온라인 서비스 구축 후(VPC, 도커, ECS 등을 이용한 오토스케일링과 CI/CD 는 적용되어야 함)
   침입 탐지 및 대응 시스템 구축 (IDS) : AWS GuardDuty로 위협 탐지 및 알람 설정, AWS Lambda와 SNS를 활용하여 이상 활동 탐지 시 즉각적인 알림 및 대응 시스템 구축

2. 온라인 서비스 구축 후(VPC, 도커, ECS 등을 이용한 오토스케일링과 CI/CD 는 적용되어야 함)
   보안 로깅 및 모니터링 환경 구축 : AWS CloudWatch, CloudTrail, Elasticsearch 등을 이용하여 통합 보안 로깅 환경 구축, SIEM(Security Information and Event Management) 시스템 

---

이메일 : blockenters@gmail.com

강의 소개 : AWS를 왜 배우는가? 

온프레미스와 클라우드 : https://vision-ai.tistory.com/entry/On-Premise-%EC%99%80-Cloud-Services

AWS 회원가입 : 모바일에서 회원가입을 진행하세요.

ec2 생성하기

ec2에 접속하기 : https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/connection-prereqs-general.html

로컬 컴퓨터에 실습환경 설정 : 자바, 파이썬(미니콘다), Git, Github.com, IntelliJ, Visual Studio Code 

실습용 더미서버 제공 사이트 : https://server.prag-ai.com

---

IAM Identity Center 사용자 생성

기존 EC2 종료 후, RDS MySQL 셋팅 : https://docs.google.com/presentation/d/12Xm89yzn-Lk6eacTjSn59hXrB28Ip4waDyPfe29jXDE/edit?usp=sharing

터널링 하기 : $ ssh -i <YOUR_PRIVATE_KEY_FILE.pem> -N -L 3307:<RDS_ENDPOINT>:3306 ec2-user@<EC2_PUBLIC_IP>

DBeaver 설치 및 접속 설정

샘플 데이터베이스와 테이블 생성해 보기 

데이터베이스 유저 생성 : 유저 만드는 쿼리문.sql

음악 정보 제공 서비스를 위해, MySQL에 실습용 테이블과 데이터 생성 : 실습 파일안에 sql파일이 있음

실습 서버의 접속정보 셋팅 후 배포하기

직접 실습 : 상품 리뷰 서버 실습

---

S3 버킷 생성하고 파일 업로드 해보기 

프로그램 코드에서 S3에 파일 업로드 하기 위한 IAM 설정

실습 서버의 설정파일 셋팅 및 실행

Restful API란? : https://docs.google.com/presentation/d/1tuZvlY2PcnQw7K6u5K92FWZ5KggVbGzewf9xlaZ_uzo/edit?usp=sharing

Postman 설치

실습서버의 API 명세서 : https://juniper-snout-930.notion.site/API-1694a24679c0807fb36bcf5f92e2d3b5

Restful API 의 JWT 기반 인증

실습 : https://docs.google.com/presentation/d/1HpPvqpjlWIIg3sK4alHSHDvzHAJBaKNBfNS9L5cf4YM/edit?usp=sharing

---

VPC : https://docs.google.com/presentation/d/1nHswohu270B0KRWUp0pRLfukoKuUnKq-QeMlRapllFA/edit?usp=sharing

AWS의 보안 : https://docs.google.com/presentation/d/1-QH-_Em43W5NBJPvEBmPoHp3r-dJz5e3dEtNOWHGRTs/edit?usp=sharing

깃허브를 이용한 CI 구축 : 첫번째 서버 이용

---

ec2에 git을 이용한 프로젝트 clone / pull

ec2에 java / maven 설치

jar 파일 생성 

ALB 트래픽 분산 처리 방법 : https://docs.google.com/presentation/d/1qiZwQNCSpfTYWoqtVp5Vyie9RFke_swgdeCLKhKspYA/edit?usp=sharing

CloudWatch를 이용한 로그 확인 

AutoScaling 자동 처리 하기 

기존 ec2삭제 테스트

---

미니콘다 다운로드 페이지 : https://www.anaconda.com/download/success

파이썬 fastapi 서버 배포와 로드밸런싱 및 오토스케일링 설정하기

서버의 소스코드 변경 적용하기

Front-End 배포하기 : https://docs.google.com/presentation/d/1beEuBRascotBGD7WNCVxGRb08ilNC8pLJRCtwTHErHk/edit?usp=sharing

---

Github Actions를 이용한 배포 자동화 : https://docs.google.com/presentation/d/11PgxPF4SZFGhr823NAoYGGtZcJM44macch9xrbIxc4U/edit?usp=sharing

보안을 위한 환경 설정 파일 처리 방법 : secrets

첫번째 더미서버 자바 스프링 부트 서버 배포 : https://github.com/blockenters/sb-music-server2

두번쨰 더미서버 파이썬 fastapi 서버 배포 : https://github.com/blockenters/python-api-server

RDS를 포함한 fastapi 서버 배포 : https://github.com/blockenters/fastapi-server

---

Github Actions + Docker 를 이용한 배포 자동화 : https://docs.google.com/presentation/d/1LfobxZTzg_lcWGtyOICpTnra3VLsccoLfF_zbUSB0L0/edit?usp=sharing

오토스케일링과 도커 배포 자동화 : https://docs.google.com/presentation/d/1-AYLtbo8SXKfBTfsSnplYhcfom_hxtTQWMwFi6771R8/edit?usp=sharing








