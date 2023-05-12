const numbers =  [1, 2, 3, 4 ,5, 6, 7];

numbers.filter( n => {
    return n === 4
})

// 코딩연습 49
function validUserNames(usernames) {
    return usernames.filter( s => {
        return s.length < 10
    })
}
validUserNames(['mark', 'staceysmom1978', 'q29832128238983', 'carrie98', 'MoanaFan']);