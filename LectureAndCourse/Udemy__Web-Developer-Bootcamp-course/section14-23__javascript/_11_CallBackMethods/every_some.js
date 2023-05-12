const exams = [80, 92, 73, 88, 87, 99];

exams.every(socre => socre >= 75);

// 코딩연습 50

function allEvens (num) {
    return num.every(n => n % 2 == 0);
}
