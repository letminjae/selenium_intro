# Selenium Study 🕵️‍♂️  

이 저장소는 Python의 Selenium 패키지를 학습하며 정리한 코드와 예제들을 공유하는 공간입니다.  

## 📌 목적  
- Selenium을 활용한 웹 자동화 및 UI 테스트 학습  
- Selenium과 같이 사용되는 pytest, jenkins, openpyxl 학습
- E2E 테스트 실습 코드 및 예제 공유  

## 🛠️ 환경  
- Python 3.13
- Selenium  
- ChromeDriver / GeckoDriver 등 브라우저 드라이버  
- 가상환경(venv, conda 등) 사용 권장  

## 📂 폴더 구조  
```plaintext
📦 selenium_intro
 ┣ 📂 basics            # Selenium 기본 개념 및 예제
 ┣ 📂 homework          # 실생활에서 사용해볼만한 페이지 별 Selenium 코드 연습
 ┣ 📂 pytest            # pytest를 사용한 테스트 코드
 ┣ 📂 e2e-testing       # pytest와 Selenium을 혼합하여 테스트한 E2E 테스트 코드
 ┣ 📜 requirements.txt # 필요 라이브러리 목록
 ┗ 📜 README.md        # 저장소 소개 및 설명
```

## 📌 설치 및 실행 방법  
1. 저장소 클론  
   ```bash
   git clone https://github.com/letminjae/selenium_intro.git
   ```
2. 가상환경 생성 및 활성화 (선택)  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. 필수 패키지 설치  
   ```bash
   pip install -r requirements.txt
   ```
4. 예제 코드 실행  
   ```bash
   python3 basics/example.py
   ```

## 📚 학습 내용  
- Selenium 기본 사용법 (웹 드라이버 실행, 요소 찾기, 상호작용)  
- Pytest + Selenium 을 사용한 파이썬 자동화 테스트 구현  
- Jenkins로 코드 변경 또는 특정 시간 시 테스트 수행될 수 있도록 CI 설정
- openpyxl로 Testcase 엑셀 데이터 존재 시 fetching하여 자동화 테스트 수행

## 📌 참고 자료  
- [Selenium 공식 문서](https://www.selenium.dev/documentation/)  
- [Python Selenium API](https://selenium-python.readthedocs.io/)  
