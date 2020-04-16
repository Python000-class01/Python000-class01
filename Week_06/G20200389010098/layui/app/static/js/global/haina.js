// JavaScript Document
(function ($) {
	"use strict";

	var defaults;

	$.hainaModal = function (params) {
		params = $.extend({}, defaults, params);
		var buttons = params.buttons;

		var buttonsHtml = '', picHtml = '';
		if (buttons.length > 0) {
			buttonsHtml = '<div class="dialog-btns">';
			buttonsHtml += buttons.map(function (d, i) {
				return '<a href="javascript:;" class="haina-btn haina-btn-dialog ' + (d.className || "") + '">' + d.text + '</a>';
			}).join("");
			buttonsHtml += '</div>';
		}

		if (params.style) picHtml = '<div class="dialog-pic"><div class="icon-item dialog-' + params.style + '"></div></div>';

		var tpl = '<div class="haina-dialog haina-dialog-alert haina-dialog-anima" style="z-index:10000;">' +
			'<a href="javascript:;" class="icon iconfont haina-close-btn close-btn">&#xe603;</a>' + picHtml +
			'<div class="dialog-text">' + params.text + '</div>' + buttonsHtml +
			'</div>';

		var dialog = $.hainaOpenModal(tpl);

		dialog.find('.haina-close-btn').click(function () {
			$.hainaCloseModal();
			params.callback();
		});

		dialog.find(".haina-btn-dialog").each(function (i, e) {
			var el = $(e);
			el.click(function () {
				$.hainaCloseModal();

				if (buttons[i].onClick) {
					buttons[i].onClick();
				}
			});
		});
	};

	$.hainaOpenModal = function (tpl) {
		var mask = $('<div class="weui_mask haina-mask-alert" style="z-index:9999;"></div>').appendTo(document.body);
		mask.show();

		var dialog = $(tpl).appendTo(document.body);

		dialog.show();
		mask.addClass("weui_mask_visible");
		dialog.addClass("weui_dialog_visible");
		document.ontouchmove = function (e) { e.preventDefault(); }
		return dialog;
	}

	$.hainaCloseModal = function () {
		$(".haina-mask-alert").removeClass("weui_mask_visible").transitionEnd(function () {
			$(this).remove();
		});
		$(".haina-dialog-alert").removeClass("weui_dialog_visible").transitionEnd(function () {
			$(this).remove();
		});
		document.ontouchmove = function (e) { return true; }
	};

	$.hainaAlert = function (text, style, callback) {
		if (typeof style === 'function') {
			callback = arguments[1];
			style = undefined;
		}
		return $.hainaModal({
			text: text,
			style: style || 'success',
			buttons: [],
			callback: callback || function () { }
		});
	}

	$.hainaConfirm = function (text, style, callbackOK, callbackCancel) {
		if (typeof title === 'function') {
			callbackCancel = arguments[2];
			callbackOK = arguments[1];
			style = undefined;
		}
		return $.hainaModal({
			text: text,
			style: style || false,
			buttons: [
				{
					text: defaults.buttonCancel,
					className: "default",
					onClick: callbackCancel
				},
				{
					text: defaults.buttonOK,
					className: "primary",
					onClick: callbackOK
				}]
		});
	};

	defaults = $.modal.prototype.defaults = {
		title: "提示",
		text: undefined,
		style: false,
		buttonOK: "确定",
		buttonCancel: "取消",
		buttonClose: "关闭",
		buttons: [{
			text: "确定",
			className: "primary"
		}]
	};

})($);

//返回
function historyBack() {
	var url = homeUrl || false;
	if ((navigator.userAgent.indexOf('MSIE') >= 0) && (navigator.userAgent.indexOf('Opera') < 0)) { // IE
		if (history.length > 0) {
			window.history.back(-1);
			return false;
		} else {
			if (url) window.location.href = url;
		}
	} else { //非IE浏览器  
		if (navigator.userAgent.indexOf('Firefox') >= 0 ||
			navigator.userAgent.indexOf('Opera') >= 0 ||
			navigator.userAgent.indexOf('Safari') >= 0 ||
			navigator.userAgent.indexOf('Chrome') >= 0 ||
			navigator.userAgent.indexOf('WebKit') >= 0) {

			if (window.history.length > 1) {
				window.history.back(-1);
				return false;
			} else {
				if (url) window.location.href = url;
			}
		} else { //未知的浏览器  
			window.history.back(-1);
			return false;
		}
	}
}


