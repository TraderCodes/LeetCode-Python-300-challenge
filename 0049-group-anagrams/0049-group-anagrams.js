/**
 * @param {string[]} strs
 * @return {string[][]}
 */
function groupAnagrams(strs) {
  const groups = {};
  for (const str of strs) {
    const sortedStr = str.split('').sort().join('');
    if (sortedStr in groups) {
      groups[sortedStr].push(str);
    } else {
      groups[sortedStr] = [str];
    }
  }
  return Object.values(groups);
}