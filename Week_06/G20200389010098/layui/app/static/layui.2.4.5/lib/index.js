/**

 @Name：layuiAdmin iframe版主入口
 @Author：贤心
 @Site：http://www.layui.com/admin/
 @License：LPPL
    
 */

layui.extend({
  setter: 'lib/config' //配置模块
    ,
  admin: 'lib/admin' //核心模块
    ,
  view: 'lib/view' //视图渲染模块
}).define(['setter', 'admin', 'element', 'layer'], function (exports) {
  var setter = layui.setter,
    element = layui.element,
    admin = layui.admin,
    tabsPage = admin.tabsPage,
    view = layui.view

    //打开标签页
    ,
    openTabsPage = function (url, text) {
      //遍历页签选项卡
      var matchTo, tabs = $('#LAY_app_tabsheader>li'),
        path = url.replace(/(^http(s*):)|(\?[\s\S]*$)/g, '');

      tabs.each(function (index) {
        var li = $(this),
          layid = li.attr('lay-id');

        if (layid === url) {
          matchTo = true;
          tabsPage.index = index;
        }
      });

      text = text || '新标签页';

      if (setter.pageTabs) {
        //如果未在选项卡中匹配到，则追加选项卡
        if (!matchTo) {
          $(APP_BODY).html([
            '<div class="layadmin-tabsbody-item layui-show">', '<iframe src="' + url + '" frameborder="0" class="layadmin-iframe"></iframe>', '</div>'
          ].join(''));
          tabsPage.index = tabs.length;
          element.tabAdd(FILTER_TAB_TBAS, {
            title: '<span>' + text + '</span>',
            id: url,
            attr: path
          });
        }
      } else {
        // var iframe = admin.tabsBody(admin.tabsPage.index).find('.layadmin-iframe');
        // iframe[0].contentWindow.location.href = url;
        var mainframe = $("#mainframe");
        $("#iframe-loading").show();
        // console.log('刷新url', url);
        mainframe.hide().attr('src', url).load(function () {
          $("#iframe-loading").hide();
          mainframe.show();
        });
      }

      //定位当前tabs
      element.tabChange(FILTER_TAB_TBAS, url);
      admin.tabsBodyChange(tabsPage.index, {
        url: url,
        text: text
      });
    }

    ,
    APP_BODY = '#LAY_app_body',
    FILTER_TAB_TBAS = 'layadmin-layout-tabs',
    $ = layui.$,
    $win = $(window);

  //初始
  if (admin.screen() < 2) admin.sideFlexible();

  // //将模块根路径设置为 controller 目录
  // layui.config({
  //   base: setter.base + 'modules/'
  // });

  // //扩展 lib 目录下的其它模块
  // layui.each(setter.extend, function (index, item) {
  //   var mods = {};
  //   mods[item] = '{/}' + setter.base + 'lib/extend/' + item;
  //   layui.extend(mods);
  // });

  //=======================
  var layer = layui.layer,
    element = layui.element,
    Tab = {},
    lockClock = null;

  Tab.openTab = function (_this) {
    var curmenu = {
      "font": '',
      "icon": '',
      "title": '',
      "href": _this.data("url") || _this.data("href")
    }
    if (_this.data("title") != undefined) {
      curmenu.title = _this.data("title");
    } else if (_this.find("cite").length > 0) {
      curmenu.title = _this.find("cite").text();
    } else {
      curmenu.title = _this.text();
    }
    if (_this.find("i.iconfont").data("icon") != undefined) {
      curmenu.font = 'iconfont';
      curmenu.icon = _this.find("i.iconfont").data("icon");
    } else {
      curmenu.font = 'layui-icon';
      curmenu.icon = _this.find("i.layui-icon").data("icon");
    }
    window.sessionStorage.setItem("curmenu", JSON.stringify(curmenu));
    this.show(curmenu);
    return true;
  }

  Tab.show = function (curmenu) {
    if (curmenu.href == undefined) {
      return false;
    }
    // console.log('打开页面', curmenu);
    // var title = '<i class="layui-icon layui-icon-app"></i>';
    // if (curmenu.font == 'iconfont') {
    // 	title += '<i class="iconfont ' + curmenu.icon + '"></i>';
    // } else {
    // 	title += '<i class="layui-icon ' + curmenu.icon + '"></i>';
    // }
    // title += '<cite>' + curmenu.title + '</cite>';
    $("#LAY_app_tab").find('span').html(curmenu.title);
    $("#iframe-loading").show();
    $("#mainframe").hide().attr('src', curmenu.href).load(function () {
      $("#iframe-loading").hide();
      $(this).show();
    });
  }

  Tab.checkUrlRole = function () {
    // console.log('开始检查历史访问');
    try {
      var urlRole = {};
      urlRole = window.sessionStorage.getItem("system_url_role");
      if (urlRole != null) {
        urlRole = JSON.parse(urlRole);
      }
      // console.log('system_url_role',urlRole);
      if (!$.isEmptyObject(urlRole)) {
        this.show(urlRole);
      } else {
        //刷新后还原打开的窗口
        urlRole = window.sessionStorage.getItem("curmenu");
        // console.log('curmenu',urlRole);
        if (urlRole != null) {
          urlRole = JSON.parse(urlRole);
          this.show(urlRole);
        } else {
          var hash = getHashParameter();
          // console.log('读取地址栏',hash);
          if (hash && $("#hash-" + hash).length > 0) {
            var urlInfo = $("#hash-" + hash);
            urlRole = {
              "title": urlInfo.text(),
              "href": urlInfo.data("url")
            };
            this.show(urlRole);
          }
        }
      }
    } catch (e) {
      console.log('读取历史链接错误', e);
    }
  }

  Tab.checkUrlRole();

  //锁屏
  function lockPage() {
    $("#init-loading").hide();
    $("#LAY_app").hide();
    $("#lock-box").show();
    refreshTimer();
    lockClock = setInterval('refreshTimer()', 1000);
  }
  $("#lock-sys").on("click", function () {
    if (!sysLockStatus) {
      return false;
    }
    Msg.loading('正在锁定...');
    $.post(lockUrl, {
      "_t": Date.parse(new Date())
    }, function (res) {
      Msg.hide();
      if (res.status == 1) {
        sysLockStatus = 0;
        lockPage();
      } else {
        Msg.error(res.info);
      }
    }, 'json');
    return false;
  })
  // 判断是否显示锁屏
  if (!sysLockStatus) {
    lockPage();
  } else {
    var loading = $("#init-loading").find('p'),
      progress = parseInt(loading.text()),
      pro = setInterval(function () {
        progress += 1;
        if (progress > 99) {
          clearInterval(pro);
          $("#init-loading").hide();
          $("#LAY_app").show();
        } else {
          loading.text(progress + '%');
        }
      }, 20);
    $(window).on('load', function () {
      clearInterval(pro);
      $("#init-loading").hide();
      $("#LAY_app").show();
    })
  }
  $("#lock-form").on("submit", function () {
    $("#unlock").click();
    return false;
  })
  // 解锁
  $("#unlock").on("click", function () {
    var lockPwd = $("#lockPwd");
    if (lockPwd.val() == '') {
      lockPwd.focus();
      layer.msg("请输入解锁密码");
    } else {
      $.post(unLockUrl, {
        "psw": lockPwd.val()
      }, function (res) {
        if (res.status == 1) {
          sysLockStatus = 1;
          lockPwd.val('');
          layer.closeAll("page");
          $("#LAY_app").show();
          $("#lock-box").hide();
          window.clearInterval(lockClock);
          Tab.checkUrlRole();
        } else if (res.status == -1) {
          document.location = res.data.jumpUrl;
        } else {
          lockPwd.focus();
          layer.msg(res.info);
        }
      }, 'json')
    }
    return false;
  });

  //手机设备的简单适配
  var treeMobile = $('.site-tree-mobile'),
    shadeMobile = $('.site-mobile-shade')

  treeMobile.on('click', function () {
    $('body').addClass('site-mobile');
  });

  shadeMobile.on('click', function () {
    $('body').removeClass('site-mobile');
  });

  //主菜单点击事件
  $(document).on('click', '#LAY-system-side-menu a', function () {
    var that = $(this);
    return menuClick(that);
  })

  //导航菜单点击事件
  $(document).on('click', '#LAY-system-topnav-menu a', function () {
    var that = $(this);
    return menuClick(that);
  })

  function menuClick(that) {
    if (that.attr('href') == 'javascript:;' && that.data('url') == undefined) {
      return false;
    }
    //特定链接不予处理
    if (!that.hasClass('openWinFull') && !that.hasClass('openWinPop') && !that.hasClass('logout') && !that.hasClass('no-urlRole')) {
      openTab(that);
      location.hash = that.data('hash');
      try {
        window.sessionStorage.setItem("system_url_role", null);
      } catch (e) {}
    }
    return true;
  }

  //后退
  $("#top-menu-goback").on("click", function () {
    document.getElementById('mainframe').contentWindow.history.back(-1);
  })

  //前进
  $("#top-menu-forward").on("click", function () {
    document.getElementById('mainframe').contentWindow.history.go(1);
  })

  //打开新窗口
  function openTab(_this) {
    Tab.openTab(_this);
  }

  //打开通知卡片链接
  $(document).on("click", ".lobibox-notify-msg a.main", function () {
    openTab($(this));
    $(".tab-content").find(".active").find(".lobibox-close").click();
  });

  $(document).on("click", ".openWinMain", function () {
    openTab($(this));
  });

  if (socketConfig.getSocketUrl) {
    var checkNewNotice = null,
      isPaly = false,
      tipsConf = {};
    $(function () {
      var reconnectFailCount = 0,
        reconnectTimes = 3,
        showTip = true;



      function doAction(rs) {
        switch (rs.action) {
          case "member_bind_wx_ok": //绑定微信
          case "wx_user_bind_ok": //绑定微信
            try {
              mainframe.window.wxUserBindIsOk(rs);
            } catch (e) {
              // console.log("error:", e.message);
            }
            break;
          case "member_unbind_wx_ok": //解除绑定微信
          case "wx_user_unbind_ok": //解除绑定微信
            try {
              mainframe.window.wxUserUnBindIsOk(rs);
            } catch (e) {
              // console.log("error:", e.message);
            }
            break;
          case "wx_new_user_msg": //收到新的微信消息
            try {
              mainframe.window.wxNewUserMsg(rs);
            } catch (e) {
              // console.log("error:", e.message);
            }
            break;
          default:
            console.log("action", rs);
        }
      }

      function updateSysMsg(errMsg) {
        if (!showTip) {
          return false
        }
        Lobibox.notify('error', {
          delay: 3000,
          size: 'mini',
          position: 'top right',
          title: '系统消息',
          msg: errMsg
        })
      }
    });

    function checkNotice() {
      if ($(".lobibox-notify-nav-tabs").find('li').length > 0) {
        // console.log('有新通知');
        if (!isPaly) {
          audio.play();
          isPaly = true;
          winTitle.show()
        }
      } else {
        // console.log('等待中');
        if (isPaly) {
          audio.currentTime = 0;
          audio.pause();
          isPaly = false;
          winTitle.clear()
        }
        checkNewNotice = false
      }
    }

    function timer() {
      if (!checkNewNotice) {
        return false
      }
      checkNotice();
      setTimeout(timer, 1000)
    }
    var winTitle = {
      time: 0,
      title: document.title,
      timer: null,
      show: function () {
        var title = winTitle.title.replace("【　　　】", "").replace("【新消息】", "");
        winTitle.timer = setTimeout(function () {
          winTitle.time++;
          winTitle.show();
          if (winTitle.time % 2 == 0) {
            document.title = "【新消息】" + title
          } else {
            document.title = "【　　　】" + title
          }
        }, 600);
        return [winTitle.timer, winTitle.title]
      },
      clear: function () {
        clearTimeout(winTitle.timer);
        document.title = winTitle.title
      }
    };
  }
  //=======================

  view().autoRender();

  //对外输出
  exports('index', {
    openTabsPage: openTabsPage
  });
});