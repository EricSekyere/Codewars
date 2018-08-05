function isIsogram(str) {
    var strArr = str.trim().split('').map(e => e.toLowerCase());
    return new Set(strArr).size == str.trim().length;
}