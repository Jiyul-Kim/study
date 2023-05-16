const fakeRequest = (url) => {
    return new Promise((reslove, reject) => {
        const rand = Math.random()
        setTimeout(() => {
            if(rand < 0.7){
                reslove('너의 가짜 데이터다!');
            }
            reject("요청 error");
        },1000)
    })
}

fakeRequest('/dogs/1')
    .then ((data) => {
        console.log("요청이 끝났습니다.");
        console.log("data: ", data);
    })
    .catch((err) => {
        console.log("이런!", err)
    })