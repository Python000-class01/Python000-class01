(function($){$.facebox=function(data,klass){$.facebox.loading()
if(data.ajax)
fillFaceboxFromAjax(data.ajax)
else if(data.image)
fillFaceboxFromImage(data.image)
else if(data.div)
fillFaceboxFromHref(data.div)
else if($.isFunction(data))
data.call($)
else
$.facebox.reveal(data,klass)}
$.extend($.facebox,{settings:{opacity:0.2,fixed:true,resize:false,overlay:true,loadingImage:PUBLIC_URL+'css/admin/images/loading.gif',closeImage:PUBLIC_URL+'css/admin/images/closelabel.gif',imageTypes:['png','jpg','jpeg','gif'],faceboxHtml:'\
    <div id="facebox" style="display:none;"> \
      <div class="popup"> \
        <table> \
          <tbody> \
            <tr> \
              <td class="tl"/><td class="b"/><td class="tr"/> \
            </tr> \
            <tr> \
              <td class="b"/> \
              <td class="body"><div class="toper"> \
                  <a href="javascript:;" class="close"> \
                    <img src="'+PUBLIC_URL+'css/admin/images/closelabel.gif" title="关闭" class="close_image" /> \
                  </a> \
                </div><div class="content"> \
                </div></td> \
              <td class="b"/> \
            </tr> \
            <tr> \
              <td class="bl"/><td class="b"/><td class="br"/> \
            </tr> \
          </tbody> \
        </table> \
      </div> \
    </div>'},loading:function(){init()
if($('#facebox .facebox-loading').length==1)
return true
showOverlay()
$('#facebox .content').empty()
$('#facebox .body').children().hide().end().append('<div class="facebox-loading"><img src="'+$.facebox.settings.loadingImage+'"/></div>')
$.facebox.fixed();$('#facebox').show()
$(document).bind('keydown.facebox',function(e){if(e.keyCode==27)
$.facebox.close()
return true})
$(document).trigger('facebox-loading.facebox')},reveal:function(data,klass){$(document).trigger('beforeReveal.facebox')
if(klass)
$('#facebox .content').addClass(klass)
$('#facebox .content').append(data)
$('#facebox .facebox-loading').remove()
$('#facebox .body').children().fadeIn('normal')
$('#facebox').css('left',$(window).width()/2-($('#facebox table').width()/2))
$(document).trigger('reveal.facebox').trigger('afterReveal.facebox')},close:function(){$(document).trigger('close.facebox')
return false},fixed:function(){$('#facebox').css({top:getPageScroll()[1]+(getPageHeight()/10),left:$(window).width()/2-($('#facebox').width()/2)})}})
$.fn.facebox=function(settings){init(settings)
function clickHandler(){$.facebox.loading(true)
var klass=this.rel.match(/facebox\[?\.(\w+)\]?/)
if(klass)
klass=klass[1]
fillFaceboxFromHref(this.href,klass)
return false}
return this.click(clickHandler)}
function init(settings){if($.facebox.settings.inited)
return true
else
$.facebox.settings.inited=true
$(document).trigger('init.facebox')
makeCompatible()
var imageTypes=$.facebox.settings.imageTypes.join('|')
$.facebox.settings.imageTypesRegexp=new RegExp('\.'+imageTypes+'$','i')
if(settings)
$.extend($.facebox.settings,settings)
$('body').append($.facebox.settings.faceboxHtml)
var preload=[new Image(),new Image()]
preload[0].src=$.facebox.settings.closeImage
preload[1].src=$.facebox.settings.loadingImage
$('#facebox').find('.b:first, .bl, .br, .tl, .tr').each(function(){preload.push(new Image())
preload.slice(-1).src=$(this).css('background-image').replace(/url\((.+)\)/,'$1')})
$('#facebox .close').click($.facebox.close)
$('#facebox .close_image').attr('src',$.facebox.settings.closeImage);if($.facebox.settings.fixed){$(window).scroll(function(){$.facebox.fixed();});}
if($.facebox.settings.resize){$(window).resize(function(){$.facebox.fixed();})}}
function getPageScroll(){var xScroll,yScroll;if(self.pageYOffset){yScroll=self.pageYOffset;xScroll=self.pageXOffset;}else if(document.documentElement&&document.documentElement.scrollTop){yScroll=document.documentElement.scrollTop;xScroll=document.documentElement.scrollLeft;}else if(document.body){yScroll=document.body.scrollTop;xScroll=document.body.scrollLeft;}
return new Array(xScroll,yScroll)}
function getPageHeight(){var windowHeight
if(self.innerHeight){windowHeight=self.innerHeight;}else if(document.documentElement&&document.documentElement.clientHeight){windowHeight=document.documentElement.clientHeight;}else if(document.body){windowHeight=document.body.clientHeight;}
return windowHeight}
function makeCompatible(){var $s=$.facebox.settings
$s.loadingImage=$s.loading_image||$s.loadingImage
$s.closeImage=$s.close_image||$s.closeImage
$s.imageTypes=$s.image_types||$s.imageTypes
$s.faceboxHtml=$s.facebox_html||$s.faceboxHtml}
function fillFaceboxFromHref(href,klass){if(href.match(/#/)){var url=window.location.href.split('#')[0]
var target=href.replace(url,'')
$.facebox.reveal($(target).clone().show(),klass)}else if(href.match($.facebox.settings.imageTypesRegexp)){fillFaceboxFromImage(href,klass)}else{fillFaceboxFromAjax(href,klass)}}
function fillFaceboxFromImage(href,klass){var image=new Image()
image.onload=function(){$.facebox.reveal('<div class="image"><img src="'+image.src+'" /></div>',klass)}
image.src=href}
function fillFaceboxFromAjax(href,klass){$.get(href,{"facebox":1},function(data){$.facebox.reveal(data,klass)})}
function skipOverlay(){return $.facebox.settings.overlay==false||$.facebox.settings.opacity===null}
function showOverlay(){if(skipOverlay())
return
if($('facebox_overlay').length==0)
$("body").append('<div id="facebox_overlay" class="facebox_hide"></div>')
$('#facebox_overlay').hide().addClass("facebox_overlayBG").css('opacity',$.facebox.settings.opacity).click(function(){$(document).trigger('close.facebox')}).fadeIn(200)
return false}
function hideOverlay(){if(skipOverlay())
return
$('#facebox_overlay').fadeOut(200,function(){$("#facebox_overlay").removeClass("facebox_overlayBG")
$("#facebox_overlay").addClass("facebox_hide")
$("#facebox_overlay").remove()})
return false}
$(document).bind('close.facebox',function(){$(document).unbind('keydown.facebox')
$('#facebox').fadeOut(function(){$('#facebox .content').removeClass().addClass('content')
hideOverlay()
$('#facebox .facebox-loading').remove()})})})(jQuery);