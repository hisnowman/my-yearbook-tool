import getpass
from google import genai

def main():
    print("=== Google Gemini AI 對話工具 ===")
    
    # 讓使用者安全貼入在 Google AI Studio 取得的 API Key
    api_key = getpass.getpass("請貼上你的 Google AI Studio API Key（貼上時畫面上不會顯示文字，直接按 Enter 即可）: ").strip()

    if not api_key:
        print("錯誤：API Key 不能為空！")
        return

    # 初始化 Google AI 客戶端（自動連接 Google 伺服器，無需手動填網址）
    client = genai.Client(api_key=api_key)

    # 讓你輸入想問 AI 的問題
    prompt = input("\n請輸入你想問 Gemini 的問題: ")

    print("\n正在思考中，請稍候...")
    try:
        # 呼叫最新的 gemini-2.5-flash 模型
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("\n--- Gemini 回覆 ---")
        print(response.text)
        print("------------------\n")
    except Exception as e:
        print("\n呼叫失敗，錯誤原因：", e)

if __name__ == "__main__":
    main()