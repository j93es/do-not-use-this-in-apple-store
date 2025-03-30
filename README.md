# do-not-use-this-in-apple-store

무릇 앱등이라면 애플 스토어 mac 디스플레이에 여러 이미지를 띄워두고 싶었던 적이 있으리라 생각합니다. 하지만 개발자로서 이미지를 띄워두는 것... 개발자스럽지 못합니다. 개발자라면 무릇 ASCII 아트죠. 이미지를 ASCII 아트로 변환하는 것을 가능하게 하기 위해서 이 프로젝트를 만들었습니다.

## Result

![result](/asset/result.png)

## Useage

1. Recommand for shy dev

```script
git clone https://github.com/j93es/do-not-use-this-in-apple-store.git
cd do-not-use-this-in-apple-store
make
```

2. Init

```script
git clone https://github.com/j93es/do-not-use-this-in-apple-store.git
cd do-not-use-this-in-apple-store
make install
```

3. Makefile cmd description

- make
  Download packages and use pre-prepared images.

  ```script
  make
  ```

- install
  Download packages

  ```script
  make install
  ```

- run
  Use your own image

  ```script
  make run IMG=/your/img/path/img.png
  ```

- help
  Makefile cmd description

  ```script
  make help
  ```

## More

1. Test

- 실제 apple store mac 환경에서 돌아가는지는 테스트해보지 않았으며, 테스트하지 않을 예정입니다.

2. Contact

- 디렉토리 삭제를 원하신다면 j93es@naver.com으로 연락주시길 바라겠습니다.
