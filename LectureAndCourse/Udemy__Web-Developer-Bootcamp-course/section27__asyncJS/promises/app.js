const promise = new Promise((resolve, reject) => {
    console.log("doing something.. .");
    setTimeout(() => {
        // resolve('jiyul');
        reject(new Error('네트워크가 연결되지 않았습니다.'))
    }, 2000);
});
promise
    .then((value) => {
    console.log((value));
    })
    .catch(error => {
        console.log(error);
    })
    .finally(() => {
        console.log('finally')
    })