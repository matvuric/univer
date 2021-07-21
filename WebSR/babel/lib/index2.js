"use strict";

var _namer = _interopRequireDefault(require("./namer2"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var person = new _namer["default"]();
console.log(person.getFullName());