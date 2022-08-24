from google.cloud import translate

class translate_language:
  @staticmethod
  def translation(string, target_lang="de"):
    client = translate.TranslationServiceClient()
    response = client.translate_text(
      contents = [string],
      target_language_code=target_lang
    )
    for translation in response.translations:
       return translation.translated_text)

