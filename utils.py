def advanced_cot_template(client,query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system","content": "you are advenced resoning system" },
            {"role": "user","content": f"""
            다음 문제를 단계별로 풀어주세요, 답변 후 스스로 검토해 오류를 수정하세요, 400자이내로 답변하세요.
            {query}
            1. 변수 정의.
            2. 방정식 설정.
            3. 계산 과정.
            4. 검토.
            5. 최종답변은 "사과: x원, 오렌지: x원" 형식으로 작성하세요.
            """}
                
        ],
        max_tokens=400,
        temperature = 0.7
    )
    return response.choices[0].message.content


def few_shot_cot(client,query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system","content": "you are few shot resoning system" },
            {"role": "user","content": f"""
            다음 문제를 few shot으로 단계별로 풀어주세요, 아래 예제를 참고해 단계별로 답변하세요. 
            답변 후 스스로 검토해 오류를 수정하세요
            
            예제 1 : 
            예제 2 :  
             

            이제 문제 풀기 
            {query}
            1. 변수 정의.
            2. 방정식 설정.
            3. 계산 과정.
            4. 검토.
            5. 최종 답변.
            """}
                
        ],
        max_tokens=400,
        temperature = 0.7
    )
    return response.choices[0].message.content
