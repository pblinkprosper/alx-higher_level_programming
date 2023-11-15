#!/usr/bin/node
exports.esrever = function (list) {
  const n_list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    n_list.push(list[i]);
  }
  return n_list;
};
