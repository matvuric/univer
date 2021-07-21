"use strict";

var _moment = _interopRequireDefault(require("moment"));

var _name = _interopRequireDefault(require("./name"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

console.log(_name["default"]);
console.log(_moment["default"].unix('1500514362').format('DD.MM.YYYY HH:mm:ss'));