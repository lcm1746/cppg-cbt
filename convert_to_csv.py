import pandas as pd

# 엑셀 파일을 CSV로 변환
try:
    df = pd.read_excel('cppg_qa_final.xlsx')
    df.to_csv('cppg_qa_final.csv', index=False, encoding='utf-8')
    print("CSV 파일 생성 완료: cppg_qa_final.csv")
    print(f"총 {len(df)} 행 변환됨")
except Exception as e:
    print(f"변환 오류: {e}") 