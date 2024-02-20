a1 = 'Мы используем файлы cookie, чтобы обеспечивать правильную работу нашего веб-сайта, персонализировать рекламные объявления и другие материалы, обеспечивать работу функций социальных сетей и анализировать сетевой трафик.'
a2 = 'Używamy plików cookie, aby zapewnić prawidłowe działanie naszej witryny, personalizować reklamy i inne treści, zapewniać funkcje mediów społecznościowych oraz analizować ruch online.'
a3 = '당사는 웹사이트가 제대로 작동하도록 하고, 광고 및 기타 콘텐츠를 개인화하고, 소셜 미디어 기능을 제공하고, 온라인 트래픽을 분석하기 위해 쿠키를 사용합니다.'
a4 = 'We use cookies to make our website function properly, personalize ads and other content, provide social media features and analyze our online traffic.'
a5 = 'колесо ключ cookie to make'


from langdetect import detect
from langdetect import detect_langs


print(detect(a1))
print(detect(a2))
print(detect(a3))
print(detect(a4))

print(detect_langs(a1))
print(detect_langs(a2))
print(detect_langs(a3))
print(detect_langs(a4))
print(detect_langs(a5))
