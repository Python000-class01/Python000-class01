
var asdasd=function(asd){
return asd+"asdasdasd";
}


layui.define(function(exports){
  var obj = {
    template: function(tpl_name){
      return asdasd(tpl_name);
    }
  };
  
  //输出test接口
  exports('test2', obj);
});  