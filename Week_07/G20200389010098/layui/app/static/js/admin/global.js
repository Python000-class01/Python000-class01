//自定义插件函数
layui.use(['layer'], function(){
    layer = layui.layer
});
$(function () {
    $('a[rel*=pop]').facebox();
    //打开全屏弹窗
    $(document).on('click', ".openWinFull", function () {
        var that = $(this),
            title = that.data('title') || that.text(),
            url = that.data('url') || that.attr('href');
        openWinFull(title, url);
        return false;
    });
	

	
	

    //打开指定宽高弹窗
    $(document).on('click', ".openWinPop", function () {
        var that = $(this),
            title = that.data('title') || that.text(),
            url = that.data('url') || that.attr('href'),
            w = that.data('width') || 800,
            h = that.data('height') || 450;
        openWinPop(title, url, w, h)
        return false;
    });
    //直接跳转到指定链接
    $(document).on('click', ".openUrl", function () {
        var that = $(this),
            _href = that.data('url') || that.attr('href');
        if (_href) {
            document.location = _href;
        }
    })
    //退出登录
    $(document).on('click', ".logout", function () {
        var that = $(this),
            _href = that.data('url') || that.attr('href');
        var index = layer.confirm('确认退出系统吗?', {
            btn: ['确认', '取消']
        }, function () {
			sessionStorage.setItem('curmenu', '');
			sessionStorage.setItem('system_url_role', '');
            top.location = _href;
        }, function () {

        });
        return false;
    })
    //全局链接进行访问记录，方便刷新后直接定位页面
    $(document).on('click', 'a', function () {
        var that = $(this);
        if (that.hasClass("openWinFull") || that.hasClass("openWinPop") || that.hasClass("openWin") || that.hasClass("logout") || that.hasClass("no-urlRole")) {
            return true;
        }
        if (that.attr('target') == '_blank') {
            return true;
        }
        var href = $(this).data('url') || $(this).attr('href'),
            title = $(this).data('title') || $(this).text();
        if (!href || typeof (href.toLocaleLowerCase()) == 'undefined' || href.toLocaleLowerCase().indexOf("javascript:") != -1) {
            console.log('路由写入跳过', href);
            return true;
        }
        try {
            window.sessionStorage.setItem("system_url_role", JSON.stringify({
                "href": href,
                "title": title
            }));
        } catch (e) {
            console.log('路由写入失败', e);
        }
    })
	
	//
	$(".btn-group button").click(function(){
	    $(this).siblings(".dropdown-menu").show();
	});
	//
	

	
})
//下拉菜单直接跳转页面
function openSelectUrl(data) {
    var that = $(data.elem[data.elem.selectedIndex]),
        _href = that.data('url') || that.attr('href');
    if (_href) {
        document.location = _href;
    }
}
/**
 * 获取hash参数
 */
function getHashParameter() {
    var arr = (location.hash || "").replace(/^\#/, '');
    return arr;
}
//时间比较
function compareTime(startDate, endDate) {
    if (startDate.length > 0 && endDate.length > 0) {
        var startDateTemp = startDate.split(" ");
        var endDateTemp = endDate.split(" ");

        var arrStartDate = startDateTemp[0].split("-");
        var arrEndDate = endDateTemp[0].split("-");

        var arrStartTime = startDateTemp[1].split(":");
        var arrEndTime = endDateTemp[1].split(":");

        var allStartDate = new Date(arrStartDate[0], arrStartDate[1], arrStartDate[2], arrStartTime[0], arrStartTime[1], arrStartTime[2]);
        var allEndDate = new Date(arrEndDate[0], arrEndDate[1], arrEndDate[2], arrEndTime[0], arrEndTime[1], arrEndTime[2]);
        if ((allEndDate.getTime() - allStartDate.getTime()) >= 60000) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

function openWinFull(title, url) {
    var index = layer.open({
        type: 2,
        title: title,
        content: url,
        success: function (layero, index) {
            setTimeout(function () {
                layui.layer.tips('点击此处返回上一页', '.layui-layer-setwin .layui-layer-close', {
                    tips: 3
                });
            }, 500)
        }
    });
    layer.full(index);
}

function openWinPop(title, url, w, h) {
    w = w || 800;
    h = h || 500;
    layer_show(title, url, w, h);
}
/*弹出层*/
function layer_show(title, url, w, h) {
	console.log(url);
    if (title == null || title == '') {
        title = false;
    };
    if (url == null || url == '') {
        url = "404.html";
    };
    if (w == null || w == '') {
        w = 800;
    };
    if (h == null || h == '') {
        h = ($(window).height() - 50);
    };
	//console.log(layer);
	console.log(url);
    layer.open({
        type: 2,
        area: [w + 'px', h + 'px'],
        fix: true,
        scrollbar: false,
        maxmin: true,
        shade: 0.4,
        title: title,
        content: url, //重点1
	    success: function(layero){
		    layer.setTop(layero); //重点2
	    }
    });
}
/*关闭弹出框口*/
function layer_close() {
    var index = parent.layer.getFrameIndex(window.name);
    parent.layer.close(index);
}
//生成真实完整链接
function U(url, str) {
    if (url.indexOf("?") > 0) {
        return url + '&' + parseParam(str);
    } else {
        return url + '?' + parseParam(str);
    }
}
//将json转换成url参数串
function parseParam(param, key) {
    var key = key || null;
    var paramStr = "";
    if (param instanceof String || param instanceof Number || param instanceof Boolean) {
        paramStr += "&" + key + "=" + encodeURIComponent(param);
    } else {
        $.each(param, function (i) {
            var k = key == null ? i : key + (param instanceof Array ? "[" + i + "]" : "." + i);
            paramStr += '&' + parseParam(this, k);
        });
    }
    return paramStr.substr(1);
};

function z(astr, str2) {
    if (typeof astr == 'object') {
        console.dir(astr);
    } else {
        str2 = str2 || '';
        console.log(astr, str2);
    }
}
/*textarea 字数限制*/
function textarealength(obj, maxlength) {
    var v = $(obj).val();
    var l = v.length;
    if (l > maxlength) {
        v = v.substring(0, maxlength);
        $(obj).val(v);
    }
    $(obj).parent().find(".textarea-length").text(v.length);
}
//获取出生日期
function getBirthdayByIdCard(UUserCard) {
    return UUserCard.substring(6, 10) + "-" + UUserCard.substring(10, 12) + "-" + UUserCard.substring(12, 14);
}

function IdentityCodeValid(code) {
    var city = {
        11: "北京",
        12: "天津",
        13: "河北",
        14: "山西",
        15: "内蒙古",
        21: "辽宁",
        22: "吉林",
        23: "黑龙江 ",
        31: "上海",
        32: "江苏",
        33: "浙江",
        34: "安徽",
        35: "福建",
        36: "江西",
        37: "山东",
        41: "河南",
        42: "湖北 ",
        43: "湖南",
        44: "广东",
        45: "广西",
        46: "海南",
        50: "重庆",
        51: "四川",
        52: "贵州",
        53: "云南",
        54: "西藏 ",
        61: "陕西",
        62: "甘肃",
        63: "青海",
        64: "宁夏",
        65: "新疆",
        71: "台湾",
        81: "香港",
        82: "澳门",
        91: "国外"
    };
    var tip = "";
    var pass = true;

    if (!code || !/^\d{6}(18|19|20)?\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|X)$/i.test(code)) {
        tip = "身份证号格式错误";
        pass = false;
    } else if (!city[code.substr(0, 2)]) {
        tip = "地址编码错误";
        pass = false;
    } else {
        //18位身份证需要验证最后一位校验位
        if (code.length == 18) {
            code = code.split('');
            //∑(ai×Wi)(mod 11)
            //加权因子
            var factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2];
            //校验位
            var parity = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2];
            var sum = 0;
            var ai = 0;
            var wi = 0;
            for (var i = 0; i < 17; i++) {
                ai = code[i];
                wi = factor[i];
                sum += ai * wi;
            }
            var last = parity[sum % 11];
            if (parity[sum % 11] != code[17]) {
                tip = "校验位错误";
                pass = false;
            }
        }
    }
    return pass;
}
//生成指定的验证规则
function getUserVerify() {
    return {
        //数组的两个值分别代表：[正则匹配、匹配不符时的提示文字]
        money: [
            /(^[1-9]([0-9]+)?(\.[0-9]{1,2})?$)|(^(0){1}$)|(^[0-9]\.[0-9]([0-9])?$)/, '金额输入不正确'
        ]
    };
}
//产生随机数函数
function getRandInt(n) {
    var rnd = "";
    for (var i = 0; i < n; i++) {
        rnd += Math.floor(Math.random() * 10);
    }
    return rnd;
}