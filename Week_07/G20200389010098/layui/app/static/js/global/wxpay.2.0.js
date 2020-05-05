// 微信支付
function wxPay(option) {
	var pay = new Object();
	pay.opt = {
		saveLogUrl: option.saveLogUrl || '',
		hash: option.hash || '',
		tryMaxCount: option.tryMaxCount || 3,
		payUrl: option.payUrl || null,
		payOkUrl: option.payOkUrl || null,
		checkOrderPayUrl: option.checkOrderPayUrl || null
	}, pay.jsApiParameters = {}, pay.tryCount = 0, pay.orderOutTradeNo = '',
		//错误日志
		pay.saveLog = function (msg) {
			$.post(pay.opt.saveLogUrl, {
				"out_trade_no": pay.orderOutTradeNo,
				"message": msg,
				"__hash__": pay.opt.hash
			}, function (res) {});
		},
		//调用微信JS api 支付
		pay.jsApiCall = function () {
			Msg.hide();
			try {
				WeixinJSBridge.invoke('getBrandWCPayRequest', pay.jsApiParameters, function (res) {
					var errMsg=res.err_msg;
					WeixinJSBridge.log('errMsg',errMsg);
					errMsg=errMsg;
					if (errMsg == 'get_brand_wcpay_request:ok') {
						pay.checkOrderPayStatus();
					} else if (errMsg == "get_brand_wcpay_request:cancel") {
						//取消支付
						Msg.alert('取消支付');
					} else if (errMsg == "get_brand_wcpay_request:fail") {
						//支付失败
						Msg.alert('支付失败');
					} else {
						Msg.alert('支付发起失败:' + errMsg);
						pay.saveLog(errMsg);
					}
				});
			} catch (e) {
				var errMsg = '支付失败:' + e;
				Msg.alert(errMsg);
				pay.saveLog(errMsg);
				return false;
			}
		},
		pay.checkOrderPayStatus = function () {
			if (pay.opt.tryCount >= pay.opt.tryMaxCount) {
				Msg.hide();
				return false;
			}
			pay.opt.tryCount += 1;
			Msg.loading('检查支付结果...');
			$.post(pay.opt.checkOrderPayUrl, {
				"out_trade_no": pay.orderOutTradeNo,
				"__hash__": pay.opt.hash
			}, function (res) {
				Msg.hide();
				switch (res.status) {
					case 0:
						Msg.alert(res.info);
						return false;
						break;
					case 1:
						Msg.alert('支付成功，即将返回...');
						$("#trade_state_str").html('支付成功');
						setTimeout(function () {
							document.location = pay.opt.payOkUrl;
						}, 2000);
						return true;
						break;
					case 2:
						Msg.loading('正在核对信息');
						setTimeout(function () {
							pay.checkOrderPayStatus();
						}, 1800);
						break;
				}
			},'json');
		},
		pay.callpay = function () {
			if (typeof WeixinJSBridge == "undefined") {
				if (document.addEventListener) {
					document.addEventListener('WeixinJSBridgeReady', pay.jsApiCall, false);
				} else if (document.attachEvent) {
					document.attachEvent('WeixinJSBridgeReady', pay.jsApiCall);
					document.attachEvent('onWeixinJSBridgeReady', pay.jsApiCall);
				}
			} else {
				pay.jsApiCall();
			}
		}, 
		pay.setOrder = function (data, callback) {
			callback = callback || null;
			Msg.loading('正在处理...');
			$.post(pay.opt.payUrl, data, function (res) {
				Msg.hide();
				if (res.status == 1) {
					pay.orderOutTradeNo = res.data.out_trade_no;
					try {
						pay.jsApiParameters = jQuery.parseJSON(res.data.jsApiParameters);
						console.log(pay.jsApiParameters);
					} catch (e) {
						Msg.alert('数据解析失败');
						callback && callback(0, res);
						return false;
					}
					Msg.loading('请求支付中...');
					pay.callpay();
					callback && callback(1, res);
				} else {
					Msg.alert(res.info);
					callback && callback(0, res);
					return false;
				}
			}, 'json');
		}
		return pay;
}