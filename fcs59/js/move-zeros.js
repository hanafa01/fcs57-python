function move_zeros(nums) {
  let l = [];

  for (let x of nums) {
    if (x !== 0) {
      l.push(x);
    }
  }

  let count_zeros = nums.length - l.length;

  for (let i = 0; i < count_zeros; i++) {
    l.push(0);
  }
  return l;
}

console.log(move_zeros([1, 2, 0, 5, 0, 11, 3, 0, 56]))