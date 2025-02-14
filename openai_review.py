
import openai

# API anahtarını burada belirt
OPENAI_API_KEY = "Your OPENAI key"

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def ai_code_review(code, performance_results):
    """OpenAI API kullanarak kod hakkında yorum yapar."""
    prompt = f"""
    Aşağıdaki Python kodunu incele ve performans açısından yorum yap:
    
    {code}

    İşte kodun performans analizi:
    {performance_results}

    Hangi iyileştirmeler yapılabilir? Daha iyi bir algoritma önerir misin?
    """
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Sen deneyimli bir Python kod performans analiz uzmanısın."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
