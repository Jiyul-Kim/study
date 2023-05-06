## 0505 노마드코더 코코아톡 챌린지 12일차
### 새로 안 사실이나 찾아서 해결한 것 정리

---


1. 글자 사이 간격(자간)
``` css
letter-spacing
```
 으로 조절

2. 이미지 위에 플레이 한 거 같이 표현하는거

    2-1. play 라는 div 새로 만들어서, 그걸 포지션 relative로 해준다. 그 다음 그 플레이 아이콘의 포지션을 absolute로 바꿔줘서 해결

    2-2. 이미지 어둡게 만들어주기
    ```css
    img {
        filter: brightness(60%)
    }
    ```

3. 이미지 블러하면 가장자리도 블러 처리가 돼서 상위 콘테이너에 맞춰지지 않음.
```css
.imageContainer {
overflow: hidden;
}    
img {
+transform:scale(1.1);
}
```