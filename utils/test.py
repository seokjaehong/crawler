< !DOCTYPE
html >
< html
lang = "ko" >
< head >
< meta
content = "text/html; charset=utf-8"
http - equiv = "Content-Type" / >
< meta
content = "IE=edge,chrome=1"
http - equiv = "X-UA-Compatible" / >
< title > Melon::음악이
필요한
순간, 멜론 < / title >
< meta
content = "음악서비스, 멜론차트, 멜론TOP100, 최신음악, 인기가요, 뮤직비디오, 앨범, 플레이어, 스트리밍, 다운로드, 아티스트플러스, 아티스트채널"
name = "keywords" / >
< meta
content = "국내 최대 1,000만곡 확보 No.1 음악사이트, 멜론! 최신음악과 실시간 차트는 기본, 내 취향을 아는 똑똑한 추천 라디오, 내가 좋아하는 아티스트의 새로운 소식까지 함께 즐겨보세요."
name = "description" / >
< meta
content = "f13fc46b807bef984aa341efeb1adec8de12264c"
name = "naver-site-verification" / >
< meta
content = "357952407588971"
property = "fb:app_id" / >
< meta
content = "Melon"
property = "og:title" / >
< meta
content = "http://cdnimg.melon.co.kr/resource/image/web/common/logo_melon142x99.png"
property = "og:image" / >
< meta
content = "음악이 필요한 순간, 멜론"
property = "og:description" / >
< meta
content = "http://www.melon.com/search/artist/index.htm?q=%EC%95%84%EC%9D%B4%EC%9C%A0&amp;section=&amp;searchGnbYn=Y&amp;kkoSpl=N&amp;kkoDpType=&amp;ipath=srch_form"
property = "og:url" / >
< meta
content = "website"
property = "og:type" / >
< meta
content = "width=device-width"
name = "viewport" / >
< link
href = "/favicon.ico?2"
id = "favicon"
rel = "shortcut icon"
type = "image/x-icon" / >
< script
type = "text/javascript" >
checkWin8Metro();
function
checkWin8Metro()
{
    var
userAgent = navigator.userAgent.toLowerCase();
var
canRunActiveX = false;
try
    {
        canRunActiveX = !!new
    ActiveXObject("htmlfile");
    }
    catch(e)
    {
        canRunActiveX = false;
    }
    if ((userAgent.indexOf("windows nt 6.2") >= 0 | | userAgent.indexOf("windows nt 6.3") >= 0) & & userAgent.indexOf(
            "msie") >= 0)
        {
        // windows
        8
        if (canRunActiveX == false)
        {
            document.location.href = "http://t.melon.com";
        }
        }
        }
        < / script >
            < script
        src = "/resource/script/web/common/jquery-1.9.1.min.js"
        type = "text/javascript" > < / script >
                                       < script
        src = "//member.melon.com/resource/script/web/member/melonweb_member_external.js?tm=20180115"
        type = "text/javascript" > < / script >
                                       < script
        src = "/resource/script/web/chart/highcharts_3.0.1.js"
        type = "text/javascript" > < / script >
                                       < link
        href = "/resource/style/web/common/melonweb_layout.css"
        rel = "stylesheet"
        type = "text/css" / >
               < link
        href = "/resource/style/web/common/melonweb_comm.css"
        rel = "stylesheet"
        type = "text/css" / >
               < link
        href = "/resource/style/web/search/melonweb_search.css?tm=2017083111"
        rel = "stylesheet"
        type = "text/css" / >
               < script
        src = "/resource/script/web/common/personal_area.js?v1"
        type = "text/javascript" > < / script >
                                       < script
        type = "text/javascript" >
        // 140423
        _추가
        MelonPersonal.respond = false;
        MelonPersonal.init(false);

        (function() {
        WEBPOCIMG = {
        defaultImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 500;
        var thumbType = "_500";
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_500";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },

        defaultAlbumImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 500;
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_500";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },

        defaultArtistImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 300;
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_300";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noArtist" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },
        defaultDjImg: function(obj)
        {
        },
        defaultMvImg: function(obj, width, height)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (height == null | | height == '') height = $(obj).height();

        var ratio43 = Math.floor((4 / 3) * 10) / 10;
        var ratio169 = Math.floor((16 / 9) * 10) / 10;
        var ratioObj = Math.floor((width / height) * 10) / 10;

        var ratio = "4x3";
        if (ratioObj == ratio43){
        ratio = "4x3"; // contentsType = "mv43";
        } else if (ratioObj == ratio169){
        ratio = "16x9"; // contentsType = "mv169";
        } else {
        if (ratioObj > 1.5) ratio = "16x9";
        else ratio = "4x3";
        }

        if (width == 0) width = 640;
        if (height == 0) ratio = "16x9";

        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_" + ratio + "_640";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noMovie" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },
        defaultPlaylistImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 500;
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_500";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },
        defaultMemberImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 300;
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_300";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noArtist" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },
        defaultPhotoImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 500;
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_500";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },
        defaultShopImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();
        if (width == 0) width = 256;
        // 가장 큰사이즈로 리사이즈함
        var thumbType = "_256";
        var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noProduct" + thumbType + "_160727.jpg/melon/resize/" + width;
        if (obj.src != defaultImg){
        obj.src = defaultImg;
        }
        },
        defaultShowwingImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();

        var
        thumbType = "_256";
        if (width > 0 & & width <= 300){
        thumbType = "_256";
        } else {
        thumbType = "_313"; // 추후 조절값
        }
        altSrc = "http://cdnimg.melon.co.kr/resource/image/web/default/noShowing" + thumbType + ".jpg";
        if (obj.src != altSrc){
        obj.src = altSrc;
        }
        },
        defaultTicketImg: function(obj, width)
        {
        if (width == null | | width == '')
        width = $(obj).width();

        var
        thumbType = "_256";
        if (width > 0 & & width <= 300){
        thumbType = "_256";
        } else {
        thumbType = "_313"; // 추후 조절값
        }
        altSrc = "http://cdnimg.melon.co.kr/resource/image/web/default/noTicket" + thumbType + ".png";
        if (obj.src != altSrc){
        obj.src = altSrc;
        }
        }
        }
        , WEBELLIPSIS = {
        ellipsis: function(ellipsisObj, moreClassName, eWidth)
        {
        // 아티스트
        더보기
        for (var i = 0; i < ellipsisObj.length; i++){
        if ($(ellipsisObj).eq(i).width() > eWidth ){
        $(ellipsisObj).eq(i).parent().parent().parent().find('.' + moreClassName).show();
        }
        }
        }
        }

        // 소식함 세팅
        $.ajax({
        url: '/gnb/getNewsCount.json'
        }).done(function(data)
        {
            var
        newCount = data.NEWSCOUNT;
        if (newCount > 99){
        newCount = '99+';
        }
        if (data.NEWSCOUNT > 0){
        $('#mgs_box_id').show();
        $('#mgs_box_id .num').html(newCount);
        }
        });
        })();

        < / script >
        < / head >
        < body >
        < div


        class ="search" id="wrap" >
    < div
    id = "skip_nav" > skip
    navigation
    < ul >
    < li > < a
    href = "#gnb_menu" > 메뉴 < / a > < / li >
    < li > < a
    href = "#id_box" > 마이영역 < / a > < / li >
    < li > < a
    href = "#conts_section" > 본문 < / a > < / li >
    < li > < a
    href = "#footer" > 하단
    정보 < / a > < / li >
    < / ul >
    < / div >
    < !--  header -->
    < div
    id = "header" >
    < div
    id = "header_wrap" >
    < div


    class ="clfix" id="gnb" >

    < h1 > < a
    href = "/index.htm"
    title = "MelOn 로고 - 홈으로 이동" > < img
    alt = "MelOn 로고 이미지"
    height = "31"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/logo_melon109x31.png"
    width = "109" / > < / a > < / h1 >
    < div


    class ="gnb_mini_menu" id="gnb_menu" >

    < div


    class ="wrap_gnb_more" >

    < div


    class ="gnb_menu_more" >

    < ul >
    < li


    class ="first_child" >

    < a


    class ="menu01 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=R01&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/chart/index.htm" title="멜론차트 - 페이지 이동" > 멜론차트 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu02 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=C01&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/new/index.htm" title="최신음악 - 페이지 이동" > 최신 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu03 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=C03&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/genre/song_list.htm?classicMenuId=DP0100" title="장르음악 - 페이지 이동" > 장르 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu04 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S04&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/dj/today/djtoday_list.htm" title="멜론DJ - 페이지 이동" > 멜론DJ < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu05 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S05&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/tv/index.htm" title="멜론TV - 페이지 이동" > 멜론TV < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu06 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S07&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/artistplus/todayupdate/index.htm" title="스타포스트 - 페이지 이동" > 스타포스트 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu07 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S09&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/musicstory/today/index.htm" title="뮤직스토리 - 페이지 이동" > 뮤직스토리 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu08" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S11&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/melonaward/timeline.htm" title="뮤직어워드" > 뮤직어워드 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu09" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=C05&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/flac/index.htm" title="원음전용관" > 원음전용관 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu10" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S06&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/smartradio/index.htm" title="스마트라디오" > 스마트라디오 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu11" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=C04&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/edu/index.htm" title="어학" > 어학 < / a >

    < / li >
    < li


    class ="" >

    < a


    class ="menu12" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=V02&amp;ACTION_AF_CLICK=V1" href="http://www.melon.com/customer/announce/index.htm" title="공지사항" > 공지사항 < / a >

    < / li >
    < / ul >
    < / div >
    < button


    class ="btn_menu_more" type="button" > < span class ="odd_span" > 메뉴 더보기 < / span > < / button >

    < / div >
    < ul


    class ="sub_gnb" >

    < li


    class ="first_child" >

    < a


    class ="menu13 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S01&amp;ACTION_AF_CLICK=V1" href="javascript:MELON.WEBSVC.POC.menu.goMyMusicMain();" title="마이뮤직 - 페이지 이동" > 마이뮤직 < / a >

    < / li >
    < li >
    < a


    class ="menu14 mlog" data="LOG_PRT_CODE=1&amp;MENU_PRT_CODE=0&amp;MENU_ID_LV1=&amp;CLICK_AREA_PRT_CODE=S02&amp;ACTION_AF_CLICK=V1" href="javascript:MELON.WEBSVC.POC.menu.goFeed();" title="소식함 " >

    < span


    class ="txt" > 소식함 < / span >

    < span


    class ="msg_box" id="mgs_box_id" style="display: none;" > < span class ="num" > 0 < / span > < span class ="none" > 개 < / span > < / span >

    < / a >
    < / li >
    < / ul >
    < / div >
    < / div >
    < script
    type = "text/javascript" >
    // MelonPersonal.isResize = false;
    MelonPersonal.printLayout();
    < / script >
    < div


    class ="wrap_search_field" >

    < !-- 통합검색
    영역 -->
    < fieldset


    class ="search_field" >

    < legend > 통합검색영역 < / legend >
    < input
    id = "top_search"
    name = ""
    onkeypress = "if(event.keyCode == 13){goSearch();}"
    style = "width:374px; ime-mode:auto;"
    title = "검색 입력 편집창"
    type = "text"
    value = "아이유" / > < input
    id = "keywordLink"
    name = "keywordLink"
    type = "hidden"
    value = "" / >
    < button


    class ="btn_icon btn_auto close" id="top_search_autocomplete_toggle" title="자동검색 펼침" type="button" > < span class ="odd_span" > 자동검색 펼침 < / span > < / button > < !-- open / close 클래스 사용 -->

    < div


    class ="auto_complete" id="top_search_autocomplete" > < div class ="auto_complete_cont" style="display:block;" > < !-- 자동완성 레이어 --> < / div >

    < / div >
    < div


    class ="auto_complete" id="top_search_autocomplete_template" style="display: none;" > < !-- 자동완성 레이어 템플릿 -->

    < !-- 텍스트
    결과 -->
    < ul


    class ="text_result" >

    < li > < a


    class ="autocomplete-label" href="#" > < / a > < / li >

    < / ul >
    < !-- 섬네일
    결과 -->
    < ul


    class ="thumb_result" >

    < li


    class ="cate" > < / li >

    < li


    class ="class02" >

    < a
    href = "#" >
    < span


    class ="thumb_40" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""


    class ="autocomplete-img" height="40" width="40" / >

    < / span >
    < div


    class ="info" >

    < span


    class ="autocomplete-label" > < / span > < br / >

    < span > < span


    class ="f11 autocomplete-info" > < / span > < / span >

    < / div >
    < / a >
    < / li >
    < / ul >
    < !-- 검색어가
    없을
    때 -->
    < ul


    class ="text_result" >

    < li


    class ="result_none" >

    < span > 해당글자로
    시작하는
    단어가
    없습니다. < / span >
    < / li >
    < / ul >
    < / div >
    < button


    class ="btn_icon search_m" title="검색" type="button" > < span class ="odd_span" > 검색 < / span > < / button >

    < / fieldset >
    < form
    action = ""
    id = "searchFrm"
    method = "get"
    style = "display: none" >
    < input
    name = "q"
    type = "hidden" / >
    < input
    name = "section"
    type = "hidden" / >
    < input
    name = "searchGnbYn"
    type = "hidden"
    value = "Y" / >
    < input
    name = "kkoSpl"
    type = "hidden"
    value = "Y" / >
    < input
    name = "kkoDpType"
    type = "hidden"
    value = "" / >
    < / form >
    < !-- // 통합검색
    영역 -->
    < div


    class ="depth2_menu" >

    < ul >
    < li


    class ="first_child" >

    < a
    href = "http://www.melon.com/artistplus/finder/index.htm"
    title = "아티스트 파인더" > 아티스트
    파인더 < / a >
    < / li >
    < li


    class ="" >

    < a
    href = "http://www.melon.com/search/trend/index.htm"
    title = "키워드 트렌드" > 키워드
    트렌드 < / a >
    < / li >
    < / ul >
    < / div >
    < / div >
    < / div >
    < / div >
    < !-- // header -->
    < div


    class ="clfix" id="cont_wrap" >

    < div
    id = "conts_section" >
    < !-- contents -->
    < link
    href = "/resource/style/web/search/melonweb_search.css?tm=2017083111"
    rel = "stylesheet"
    type = "text/css" / >
    < style
    type = "text/css" >
    .d_artist_list
    b
    {color:  # 7cb710 !important; text-decoration:underline !important;}
    < / style >
        <!-- contents -->
    < div
    id = "conts" >
         < h2


    class ="none" > 아티스트 검색 < / h2 >

    < !-- 검색어
    문구 -->
    < div


    class ="search_phrse" id="search_phrse" >

    < p >
    < strong


    class ="fc_serch" > ‘아이유’ < / strong > 에 대한 검색 결과입니다.

    < / p >
    < / div >
    < !-- 검색어
    문구 -->
    < !-- 탭 -->
    < !-- 탭 -->
    < div


    class ="wrap_tab03 type09" id="divCollection" >

    < ul >
    < li


    class ="first_child" >

    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','total','searchFrm','','','N');" title="통합검색- 페이지 이동" >

    < span


    class ="cntt" > 통합검색 < / span >

    < / a >
    < / li >
    < li


    class ="on" data-coll="artist" >

    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','artist','searchFrm','','','N');" title="아티스트 - 페이지 이동" >

    < span


    class ="cntt" > 아티스트 < / span >

    < / a >
    < / li >
    < li
    data - coll = "song" >
    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','song','searchFrm','','','N');" title="곡 - 페이지 이동" >

    < span


    class ="cntt" > 곡 < / span >

    < / a >
    < / li >
    < li
    data - coll = "album" >
    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','album','searchFrm','','','N');" title="앨범 - 페이지 이동" >

    < span


    class ="cntt" > 앨범 < / span >

    < / a >
    < / li >
    < li
    data - coll = "mv" >
    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','mv','searchFrm','','','N');" title="영상 - 페이지 이동" >

    < span


    class ="cntt" > 영상 < / span >

    < / a >
    < / li >
    < li
    data - coll = "lyric" >
    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','lyric','searchFrm','','','N');" title="가사 - 페이지 이동" >

    < span


    class ="cntt" > 가사 < / span >

    < / a >
    < / li >
    < li
    data - coll = "dj" >
    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','dj','searchFrm','','','N');" title="DJ플레이리스트 - 페이지 이동" >

    < span


    class ="cntt" > DJ플레이리스트 < / span >

    < / a >
    < / li >
    < li
    data - coll = "musicstory" >
    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','musicstory','searchFrm','','','N');" title="멜론매거진 - 페이지 이동" >

    < span


    class ="cntt" > 멜론매거진 < / span >

    < / a >
    < / li >
    < !-- 2016.11
    .04
    제거 -->
    < li


    class ="last_child" data-coll="qna" >

    < a


    class ="link_tab" href="javascript:melon.link.goTotalSearch('아이유','qna','searchFrm','','','N');" title="고객지원 - 페이지 이동" >

    < span


    class ="cntt" > 고객지원 < / span >

    < / a >
    < / li >
    < / ul >
    < / div >
    < !-- // 탭 -->
    < !-- // 탭 -->
    < div


    class ="section_atist" >

    < h3


    class ="title first" > 아티스트 < strong class ="serch_totcnt" > 총 < em > 7 < / em > 건 < / strong > < / h3 >

    < div


    class ="wrap_finder_serch_cnd" >

    < div


    class ="wrap_finder_cnd" >

    < dl >
    < dt >
    < span


    class ="text" > 성별 < / span >

    < / dt >
    < dd >
    < label


    class ="on" for ="sex01" >

    < input
    checked = "checked"


    class ="input_radio" id="sex01" name="sex" type="radio" value="" / >

    < span


    class ="text" > 전체 < / span >

    < / label >
    < label
    for ="sex02" >
    < input


    class ="input_radio" id="sex02" name="sex" type="radio" value="M" / >

    < span


    class ="text" > 남성 < / span >

    < / label >
    < label
    for ="sex03" >
    < input


    class ="input_radio" id="sex03" name="sex" type="radio" value="F" / >

    < span


    class ="text" > 여성 < / span >

    < / label >
    < label
    for ="sex04" >
    < input


    class ="input_radio" id="sex04" name="sex" type="radio" value="H" / >

    < span


    class ="text" > 혼성 < / span >

    < / label >
    < / dd >
    < / dl >
    < dl >
    < dt >
    < span


    class ="text" > 활동유형 < / span >

    < / dt >
    < dd >
    < label


    class ="on" for ="act01" >

    < input
    checked = "checked"


    class ="input_radio" id="act01" name="actType" type="radio" value="" / >

    < span


    class ="text" > 전체 < / span >

    < / label >
    < label
    for ="act02" >
    < input


    class ="input_radio" id="act02" name="actType" type="radio" value="1" / >

    < span


    class ="text" > 솔로 < / span >

    < / label >
    < label
    for ="act03" >
    < input


    class ="input_radio" id="act03" name="actType" type="radio" value="2" / >

    < span


    class ="text" > 그룹 < / span >

    < / label >
    < / dd >
    < / dl >
    < dl >
    < dt >
    < span


    class ="text" > 국적 < / span >

    < / dt >
    < dd >
    < label


    class ="on" for ="ntnt01" >

    < input
    checked = "checked"


    class ="input_radio" id="ntnt01" name="domestic" type="radio" value="" / >

    < span


    class ="text" > 전체 < / span >

    < / label >
    < label
    for ="ntnt02" >
    < input


    class ="input_radio" id="ntnt02" name="domestic" type="radio" value="Y" / >

    < span


    class ="text" > 국내 < / span >

    < / label >
    < label
    for ="ntnt03" >
    < input


    class ="input_radio" id="ntnt03" name="domestic" type="radio" value="N" / >

    < span


    class ="text" > 국외 < / span >

    < / label >
    < / dd >
    < / dl >
    < dl


    class ="gnr" >

    < dt >
    < span


    class ="text" > 장르 < / span >

    < / dt >
    < dd >
    < label


    class ="on" for ="gnr01" >

    < input
    checked = "checked"


    class ="input_radio" id="gnr01" name="genreRoot" type="radio" value="" / >

    < span


    class ="text" > 전체 < / span >

    < / label >
    < label
    for ="gnr02" >
    < input


    class ="input_radio" id="gnr02" name="genreRoot" type="radio" value="0101" / >

    < span


    class ="text" > 가요 < / span >

    < / label >
    < label
    for ="gnr03" >
    < input


    class ="input_radio" id="gnr03" name="genreRoot" type="radio" value="0201" / >

    < span


    class ="text" > POP < / span >

    < / label >
    < label
    for ="gnr04" >
    < input


    class ="input_radio" id="gnr04" name="genreRoot" type="radio" value="0301" / >

    < span


    class ="text" > OST < / span >

    < / label >
    < label
    for ="gnr05" >
    < input


    class ="input_radio" id="gnr05" name="genreRoot" type="radio" value="1401" / >

    < span


    class ="text" > 일렉트로니카 / 클럽뮤직 < / span >

    < / label >
    < label
    for ="gnr06" >
    < input


    class ="input_radio" id="gnr06" name="genreRoot" type="radio" value="1501" / >

    < span


    class ="text" > 록 / 메탈 < / span >

    < / label >
    < label
    for ="gnr07" >
    < input


    class ="input_radio" id="gnr07" name="genreRoot" type="radio" value="1601" / >

    < span


    class ="text" > R & amp;B / Soul < / span >

    < / label >
    < label
    for ="gnr08" >
    < input


    class ="input_radio" id="gnr08" name="genreRoot" type="radio" value="1701" / >

    < span


    class ="text" > 랩 / 힙합 < / span >

    < / label >
    < label
    for ="gnr09" >
    < input


    class ="input_radio" id="gnr09" name="genreRoot" type="radio" value="1801" / >

    < span


    class ="text" > 인디음악 < / span >

    < / label >
    < label
    for ="gnr010" >
    < input


    class ="input_radio" id="gnr010" name="genreRoot" type="radio" value="1901" / >

    < span


    class ="text" > 트로트 < / span >

    < / label >
    < label
    for ="gnr011" >
    < input


    class ="input_radio" id="gnr011" name="genreRoot" type="radio" value="0401" / >

    < span


    class ="text" > J-POP < / span >

    < / label >
    < label
    for ="gnr012" >
    < input


    class ="input_radio" id="gnr012" name="genreRoot" type="radio" value="0501" / >

    < span


    class ="text" > 클래식 < / span >

    < / label >
    < label
    for ="gnr013" >
    < input


    class ="input_radio" id="gnr013" name="genreRoot" type="radio" value="0901" / >

    < span


    class ="text" > 재즈 < / span >

    < / label >
    < label
    for ="gnr014" >
    < input


    class ="input_radio" id="gnr014" name="genreRoot" type="radio" value="0801" / >

    < span


    class ="text" > 뉴에이지 < / span >

    < / label >
    < label
    for ="gnr015" >
    < input


    class ="input_radio" id="gnr015" name="genreRoot" type="radio" value="0701" / >

    < span


    class ="text" > 어린이 < / span >

    < / label >
    < label
    for ="gnr016" >
    < input


    class ="input_radio" id="gnr016" name="genreRoot" type="radio" value="2001" / >

    < span


    class ="text" > 태교 < / span >

    < / label >
    < label
    for ="gnr017" >
    < input


    class ="input_radio" id="gnr017" name="genreRoot" type="radio" value="0601" / >

    < span


    class ="text" > CCM < / span >

    < / label >
    < label
    for ="gnr018" >
    < input


    class ="input_radio" id="gnr018" name="genreRoot" type="radio" value="1101" / >

    < span


    class ="text" > 종교음악 < / span >

    < / label >
    < label
    for ="gnr019" >
    < input


    class ="input_radio" id="gnr019" name="genreRoot" type="radio" value="1201" / >

    < span


    class ="text" > 국악 < / span >

    < / label >
    < label
    for ="gnr020" >
    < input


    class ="input_radio" id="gnr020" name="genreRoot" type="radio" value="1301" / >

    < span


    class ="text" > 중국음악 < / span >

    < / label >
    < label
    for ="gnr021" >
    < input


    class ="input_radio" id="gnr021" name="genreRoot" type="radio" value="1001" / >

    < span


    class ="text" > 월드뮤직 < / span >

    < / label >
    < / dd >
    < / dl >
    < dl


    class ="gnr_dtl" >

    < dt >
    < span


    class ="text" > 세부장르 < / span >

    < / dt >
    < dd >
    < div


    class ="finder_wrong" >

    < p > 세부장르가
    없습니다. < / p >
    < span


    class ="wrap_vertical" > < / span >

    < / div >
    < label
    style = "display:none;" >
    < input


    class ="input_radio" name="genreCd" type="radio" value="" / >

    < span


    class ="text" > 월드 < / span >

    < / label >
    < / dd >
    < / dl >
    < / div >
    < div


    class ="wrap_finder years" > < dl >

    < dt >
    < span


    class ="text" > 활동연대 < / span >

    < / dt >
    < dd >
    < div


    class ="finder_yearlk_wrap" >

    < div


    class ="yearlk_bar bar_year" >

    < !-- 시작
    년도
    설정 -->
    < div


    class ="yearlk_bar last" style="width:0;" >

    < div


    class ="sel d_btn" title="시작년도 설정하기" > 년도 설정하기 < / div >

    < / div >
    < !-- // 시작
    년도
    설정 -->
    < !-- 마지막
    년도
    설정 -->
    < div


    class ="yearlk_bar start" style="width:588px;" >

    < div


    class ="sel d_btn" title="마지막년도 설정하기" > 년도 설정하기 < / div >

    < / div >
    < !-- // 마지막
    년도
    설정 -->
    < / div >
    < div


    class ="yearlk_text" >

    < a


    class ="first_child" href="#" title="1960년대 이전 설정 하기" > 이전 < / a >

    < a


    class ="t1960" href="#" title="1960년대 설정 하기" > 1960년 < / a >

    < a


    class ="t1970" href="#" title="1970년대 설정 하기" > 1970년 < / a >

    < a


    class ="t1980" href="#" title="1980년대 설정 하기" > 1980년 < / a >

    < a


    class ="t1990" href="#" title="1990년대 설정 하기" > 1990년 < / a >

    < a


    class ="t2000" href="#" title="2000년대 설정 하기" > 2000년 < / a >

    < a


    class ="t2010" href="#" title="2010년대 설정 하기" > 2010년 < / a >

    < a


    class ="next" href="#" title="2010년대 이후 설정 하기" > 이후 < / a >

    < / div >
    < / div >
    < div


    class ="wrap_btn" >

    < button


    class ="btn_big short calendar" title="연대적용" type="button" > < span class ="odd_span" > < span class ="even_span fc_strong" >

    < span


    class ="text" > 연대적용 < / span >

    < / span > < / span > < / button >
    < / div >
    < / dd >
    < / dl > < / div >
    < / div >
    < div


    class ="re_serch clfix" >

    < div


    class ="fl_left" >

    < strong


    class ="fc_strong" > 결과 내 재검색 < / strong >

    < span >
    < input


    class ="text" id="friend" placeholder="검색어를 입력하세요" style="width:160px;" title="아티스트 결과 내 재검색 입력 편집창" type="text" / >

    < button


    class ="btn btn_base" title="아티스트 결과 내 재검색" type="button" > < span class ="odd_span" > < span class ="even_span" > 검색 < / span > < / span > < / button >

    < / span >
    < / div >
    < ul


    class ="list_sort" >

    < li


    class ="first_child" data-sort="weight" > < a href="javascript:;" title="아티스트 리스트 정확도순으로 정렬" > 정확도 < / a > < / li >

    < li
    data - sort = "hit" > < a
    href = "javascript:;"
    title = "아티스트 리스트 인기순으로 정렬" > 인기순 < / a > < / li >
    < li
    data - sort = "ganada" > < a
    href = "javascript:;"
    title = "아티스트 리스트 가나다순으로 정렬" > 가나다순 < / a > < / li >
    < / ul >
    < / div >
    < div
    id = "pageList"
    style = "display: none" >
    < div


    class ="list_atist12 d_artist_list" >

    < ul >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','261143');melon.link.goArtistDetail('261143');" title="아이유 - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr/cm/artistcrop/images/002/61/143/261143_500.jpg?8278b340c081cd2bd020bff2d632329f/melon/resize/240/quality/80/optimize"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','261143');melon.link.goArtistDetail('261143');" title="아이유 - 페이지 이동" > < b > 아이유 < / b > < / a >

    < / dt >
    < dd


    class ="gubun" >


    대한민국 / 여성 / 솔로
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < span > Ballad < / span >, < span > Dance < / span >, < span > Drama < / span >
    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < a


    class ="btn_play_song" href="javascript:;" onclick="searchLog('web_artist','ARTIST','SO','아이유','261143');melon.play.playSong('26020102',30646585);" title="잠 못 드는 밤 비는 내리고 재생 - 새 창" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > 잠 못 드는 밤 비는 내리고 < / span >

    < / a >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="261143" name="likeFan_261143" onclick="searchLog('web_artist','ARTIST','AR','아이유','261143');" title="아이유 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_261143" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "261143" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','560205');melon.link.goArtistDetail('560205');" title="IUV - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr/cm/artistcrop/images/005/60/205/560205_500.jpg/melon/resize/240/quality/80/optimize"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','560205');melon.link.goArtistDetail('560205');" title="IUV - 페이지 이동" > IUV < / a >

    < / dt >
    < dd


    class ="gubun" >


    대한민국 / 여성 / 그룹
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < span > Dance < / span >, < span > Rap / Hip - hop < / span >
    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < a


    class ="btn_play_song" href="javascript:;" onclick="searchLog('web_artist','ARTIST','SO','아이유','560205');melon.play.playSong('26020102',3672394);" title="여기 와썹 재생 - 새 창" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > 여기 와썹 < / span >

    < / a >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="560205" name="likeFan_560205" onclick="searchLog('web_artist','ARTIST','AR','아이유','560205');" title="IUV 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_560205" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "560205" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','889388');melon.link.goArtistDetail('889388');" title="이유 갓지(GOD G) 않은 이유 (박명수, 아이유) - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr/cm/artistcrop/images/008/89/388/889388_500.jpg/melon/resize/240/quality/80/optimize"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','889388');melon.link.goArtistDetail('889388');" title="이유 갓지(GOD G) 않은 이유 (박명수, 아이유) - 페이지 이동" > 이유 갓지(GOD G) 않은 이유 (박명수, < b > 아이유 < / b > ) < / a >

    < / dt >
    < dd


    class ="gubun" >


    대한민국 / 혼성 / 그룹
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < span > Dance < / span >
    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < a


    class ="btn_play_song" href="javascript:;" onclick="searchLog('web_artist','ARTIST','SO','아이유','889388');melon.play.playSong('26020102',5826461);" title="레옹 재생 - 새 창" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > 레옹 < / span >

    < / a >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="889388" name="likeFan_889388" onclick="searchLog('web_artist','ARTIST','AR','아이유','889388');" title="이유 갓지(GOD G) 않은 이유 (박명수, 아이유) 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_889388" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "889388" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','4263');melon.link.goArtistDetail('4263');" title="박명수 - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr/cm/artistcrop/images/000/04/263/4263_500.jpg/melon/resize/240/quality/80/optimize"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','4263');melon.link.goArtistDetail('4263');" title="박명수 - 페이지 이동" > 박명수 < / a >

    < / dt >
    < dd


    class ="gubun" >


    대한민국 / 남성 / 솔로
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < span > Dance < / span >, < span > Ballad < / span >, < span > Electronica < / span >
    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < a


    class ="btn_play_song" href="javascript:;" onclick="searchLog('web_artist','ARTIST','SO','아이유','4263');melon.play.playSong('26020102',30317243);" title="Saxophone Magic (Feat. 유재환, 초희) 재생 - 새 창" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > Saxophone Magic (Feat.유재환, 초희) < / span >

    < / a >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="4263" name="likeFan_4263" onclick="searchLog('web_artist','ARTIST','AR','아이유','4263');" title="박명수 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_4263" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "4263" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','567934');melon.link.goArtistDetail('567934');" title="The Aiu - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr/cm/artistcrop/images/005/67/934/567934_500.jpg/melon/resize/240/quality/80/optimize"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','567934');melon.link.goArtistDetail('567934');" title="The Aiu - 페이지 이동" > The Aiu < / a >

    < / dt >
    < dd


    class ="gubun" >


    일본 / 혼성 / 그룹
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < span > Rock < / span >
    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < a


    class ="btn_play_song" href="javascript:;" onclick="searchLog('web_artist','ARTIST','SO','아이유','567934');melon.play.playSong('26020102',3560395);" title="Loser 재생 - 새 창" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > Loser < / span >

    < / a >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="567934" name="likeFan_567934" onclick="searchLog('web_artist','ARTIST','AR','아이유','567934');" title="The Aiu 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_567934" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "567934" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','686375');melon.link.goArtistDetail('686375');" title="로엔트리 - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','686375');melon.link.goArtistDetail('686375');" title="로엔트리 - 페이지 이동" > 로엔트리 < / a >

    < / dt >
    < dd


    class ="gubun" >


    대한민국 / 혼성 / 그룹
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < a


    class ="btn_play_song" href="javascript:;" onclick="searchLog('web_artist','ARTIST','SO','아이유','686375');melon.play.playSong('26020102',0);" title=" 재생 - 새 창" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > < / span >

    < / a >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="686375" name="likeFan_686375" onclick="searchLog('web_artist','ARTIST','AR','아이유','686375');" title="로엔트리 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_686375" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "686375" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < li >
    < div


    class ="wrap_atist12" >

    < a


    class ="thumb" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','167076');melon.link.goArtistDetail('167076');" title="아이유악대 - 페이지 이동" >

    < span


    class ="thumb_frame" > < / span >

    < img
    alt = ""
    height = "120"
    onerror = "WEBPOCIMG.defaultArtistImg(this);"
    src = "http://cdnimg.melon.co.kr"
    width = "120" / >
    < / a >
    < div


    class ="atist_info" >

    < dl >
    < dt >
    < strong


    class ="none" > 아티스트명 < / strong >

    < a


    class ="ellipsis" href="javascript:searchLog('web_artist','ARTIST','AR','아이유','167076');melon.link.goArtistDetail('167076');" title="아이유악대 - 페이지 이동" > < b > 아이유 < / b > 악대 < / a >

    < / dt >
    < dd


    class ="gubun" >


    중국 / 남성 / 솔로
    < / dd >
    < dd


    class ="gnr" >

    < strong


    class ="none" > 음악장르 < / strong >

    < div


    class ="ellipsis fc_strong" >

    < span > Rock < / span >
    < / div >
    < / dd >
    < dd


    class ="btn_play" >

    < span


    class ="btn_play_song disabled" >

    < span


    class ="icon_play" > 곡재생 < / span >

    < span


    class ="songname12" > 무법인수하거 (無法忍受下去: 참을수


    없다) < / span >
    < / span >
    < / dd >
    < dd


    class ="wrap_btn" >

    < button


    class ="btn_join_fan" data-artist-menuid="26020102" data-artist-no="167076" name="likeFan_167076" onclick="searchLog('web_artist','ARTIST','AR','아이유','167076');" title="아이유악대 팬맺기" type="button" > < span class ="odd_span" > 팬 < / span > < / button > < span class ="cnt_fan" > < span class ="cnt_span" id="d_fan_cnt_167076" > 0 < / span > < / span >

    < input
    name = "artistId"
    type = "hidden"
    value = "167076" / >
    < / dd >
    < / dl >
    < / div >
    < / div > <!-- //


    class ="wrap_atist12" -->

    < / li >
    < / ul >
    < / div >
    < script
    type = "text/javascript" >

    $(function() {
    var WEBSVC = MELON.WEBSVC;

    WEBSVC.ArtistList.init(); // 팬맺기
    var
    isTotalPage = false;
    if ('artist' == 'total'){
    isTotalPage = true;
    }
    isTotalPage = false;
    if (!isTotalPage){
    / * ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    * 팬여부 체크값 Ajax로 가져오기
    ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
    var likeArtistId = $(".wrap_btn input[name=artistId]").map(function() {
    return $(this).val();
    }).get().join(',');
    $.ajax({
    type: "POST",
    url: "/commonlike/getArtistFan.json",
    data: ({contsIds: likeArtistId}),
    async: false,
    success: function(result)
    {
        var
    listLike = result.contsFan;
    for (var i=0; i < listLike.length; i++) {
        var SUMMCNT = MELON.WEBSVC.number.addComma(listLike[i].SUMMCNT);
    $('#d_fan_cnt_'+listLike[i].CONTSID).text(SUMMCNT + '');
    if (listLike[i].LIKEYN == "Y") {
    $("button[name=likeFan_"+listLike[i].CONTSID+"]").addClass("btn_join_fan disabled on").prop('disabled', true).attr('tabIndex', 0);
    var btnTitle = $("button[name=likeFan_"+listLike[i].CONTSID+"]").attr('title').replace('팬맺기', '팬입니다');
    $("button[name=likeFan_"+listLike[i].CONTSID+"]").attr('title', btnTitle);
    } else {
    $("button[name=likeFan_"+listLike[i].CONTSID+"]").addClass("btn_join_fan");
    }
    }
    }
    });
    }

    });

    < / script >
        < script
    type = "text/javascript" >
    $(document).ready(function()
    {
    $('#pageObjNavgation').html(
        "\u003Cdiv class=\"paginate\"\u003E\u003Ca href=\"javascript:;\" class=\"btn_first disabled\"\u003E\u003Cspan\u003E맨처음\u003C\/span\u003E\u003C\/a\u003E \u003Ca href=\"javascript:;\" class=\"btn_pre disabled\"\u003E\u003Cspan\u003E이전\u003C\/span\u003E\u003C\/a\u003E \u003Cspan class=\"page_num\"\u003E\u003Cstrong\u003E\u003Cspan class=\"none\"\u003E현재페이지\u003C\/span\u003E1\u003C\/strong\u003E\u003C\/span\u003E \u003Ca href=\"javascript:;\" class=\"btn_next disabled\"\u003E\u003Cspan\u003E다음\u003C\/span\u003E\u003C\/a\u003E \u003Ca href=\"javascript:;\" class=\"btn_last disabled\"\u003E\u003Cspan\u003E맨끝\u003C\/span\u003E\u003C\/a\u003E\u003C\/div\u003E")
    });
    < / script >
        < script
    type = "text/javascript" >
    $('#pageObjNavgation').show();
    < / script >
        < script
    type = "text/javascript" >
           jQuery(function($) {
                              // 총건수
    표시
    $('.serch_totcnt em').html(MELON.WEBSVC.number.addComma('7'));
    });
    < / script >
        < / div >
            < div
    id = "pageObjNavgation"
    style = "display: none;" > < / div >
                                   < script
    src = "/resource/script/common/jquery.ba-bbq.min.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "/resource/script/common/historypager.js"
    type = "text/javascript" > < / script >
                                   < script
    type = "text/javascript" >
           var
    pageObj = new
    Pagination('listArtists.htm', 'pageList', 'pageObjNavgation', '20', 'pageObj', false);
    < / script >
        < script
    type = "text/javascript" > \
           pageObj.addParam('q', '아이유');
    pageObj.addParam('sq', '');
    pageObj.addParam('sort', 'weight');
    pageObj.addParam('section', 'all');
    pageObj.addParam('sex', '');
    pageObj.addParam('actType', '');
    pageObj.addParam('domestic', '');
    pageObj.addParam('genreCd', '');
    pageObj.addParam('actYear', '');
    < / script >
        < / div >
            < / div >
                <!-- side -->
    < div
    id = "divSearchChart" > < / div >
                                < script
    type = "text/javascript" >
    $(function() {

    var sideType = '';
    var aUrl ='/search/side/keywordChart.htm';
    // 분야별키워드 랜덤인 사이드인 경우
    if (sideType == 'trend')
    {
        aUrl = '/search/side/cateRandomChart.htm';
    }

    $.ajax({
        url: aUrl,
        data: {query: encodeURIComponent('아이유'), sideType: ''}
    }).done(function(html)
    {
    $('#divSearchChart').html(html);
    });
    });
    < / script >
        <!-- // side -->
    < !-- // contents -->
    < script
    type = "text/javascript" >
           var
    httpWww = "http://www.melon.com";
    var
    httpsWww = "https://www.melon.com";
    var
    POC_ID = "XXXX";
    < / script >
        < script
    src = "/resource/script/web/common/melonweb_openlib.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "https://cdnimg.melon.co.kr/static/web/resource/script/w1/tu/7/15u99gmdn3.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "https://cdnimg.melon.co.kr/static/web/resource/script/w1/og/7/kv18j7iqi3.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "/resource/script/web/common/MPAPI.js?tm=20171129"
    type = "text/javascript" > < / script >
                                   < script
    src = "https://cdnimg.melon.co.kr/static/web/resource/script/w1/fn/n/1y0yzmf9x67.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "https://cdnimg.melon.co.kr/static/web/resource/script/w1/jd/v/14ifiepkjxj.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "/resource/script/web/chart/json2.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "/resource/script/web/common/melonweb_zam.js?tm=2016042816"
    type = "text/javascript" > < / script >
                                   < script
    src = "https://cdnimg.melon.co.kr/static/web/resource/script/w1/8k/8/1ed5h822hvv.js"
    type = "text/javascript" > < / script >
                                   < script
    src = "https://log.melon.com/mlog.js"
    type = "text/javascript" > < / script >
                                   < script
    type = "text/javascript" >
           var
    melon = MELON.WEBSVC.POC;

    document.domain = "melon.com";

    // pocId
    쿠키설정
    실행
    try {
    melon.setPocId();
    } catch (e){}
    < / script >
    < script
    src = "/resource/script/web/common/socket.io.js"
    type = "text/javascript" > < / script >
    < script
    src = "/resource/script/web/search/melonweb_search.js"
    type = "text/javascript" > < / script >
    < script
    type = "text/javascript" >
    var
    searchLog = MELON.WEBSVC.POC.link.goSearchLog
    < / script >
    < script
    type = "text/javascript" >
    if (typeof pageObj != "undefined"){
    var _oldShow = pageObj.show;
    pageObj.show = function(){
    // 콤보설정
    // 비즈니스에 해당하는 로직을 수행(히스토리 파라메터 값에 해당하는 콤보 선택) 후, 원래 show 함수를 호출 한다.
    var jsonParam = eval(pageObj.params);

    if ($('#conts .section_no_data').length > 0 & & jsonParam.sq == ''){
    $('#conts .re_serch').hide();
    } else {
    $('#conts .re_serch').show();
    }

    _oldShow.apply(this, arguments);

    if ($('#conts .section_no_data').length > 0 ){
    $('#pageObjNavgation').hide();
    }

    $('#conts .re_serch .list_sort [data-sort].on').removeClass('on');
    $('#conts .re_serch .list_sort [data-sort='+jsonParam.sort+']').addClass('on');

    }
    }
    < / script >
    < script
    type = "text/javascript" >
    jQuery(function($) {
        var
    WEBSVC = MELON.WEBSVC;

    WEBSVC.ArtistList.init();

    // 검색어
    표시
    //$('#search_phrse .fc_serch').html(decodeURIComponent('‘아이유’'));
    // $('#search_phrse strong[class="fc_serch"]').html(decodeURIComponent('‘아이유’'));
    });
    < / script >
    < script
    type = "text/javascript" >
    jQuery(function($) {
        var
    WEBSVC = MELON.WEBSVC;

    WEBSVC.ArtistList.init();

    // 검색어
    표시
    //$('#search_phrse .fc_serch').html(decodeURIComponent('‘아이유’'));
    // $('#search_phrse strong[class="fc_serch"]').html(decodeURIComponent('‘아이유’'));

    // 정렬
    표시
    $('#conts .re_serch .list_sort [data-sort=weight]').addClass('on');

    // 아티스트
    검색
    function
    searchArtists()
    {

        var
    instance = $('div.wrap_finder_serch_cnd').artistFinder('instance');

    var
    data = instance.getValue();

    var
    period = instance.getPeriodValue();
    if (period.isYearSelected) {
    var acYear = '';
    for (var i = 0; i < period.years.length; i++) {
    var tyear = period.years[i] + '';
    if (tyear != '0') {
    tyear = tyear.substring(2, 4);
    }
    acYear += tyear + ' ';
    }
    data.actYear = acYear;
    }

    var sq = $('#conts .re_serch .fl_left input').trimVal();
    if (sq) {
    sq = encodeURIComponent(sq);
    }

    pageObj.addParam('q', '아이유');
    pageObj.addParam('sq', sq);
    pageObj.addParam('sort', $('#conts .re_serch .list_sort [data-sort].on').attr('data-sort'));
    pageObj.addParam('section', 'all');
    pageObj.addParam('sex', data.sex);
    pageObj.addParam('actType', data.actType);
    pageObj.addParam('domestic', data.domestic);
    pageObj.addParam('genreCd', data.genreCd);
    pageObj.addParam('actYear', data.actYear);
    pageObj.sendFirstPage();
    }

    // 파인더 빌드
    $('div.wrap_finder_serch_cnd').artistFinder({
    periodSelector: 'div.finder_yearlk_wrap',
                    on: {
        'artistfindersearch': function(e) {
        searchArtists();
    }
    }
    });

    // 결과
    내
    재검색 - 엔터
    키
    입력시
    $('#conts .re_serch').on('keyup', '.fl_left input', function(e)
    {
    if (e.keyCode == 13)
    {
        searchArtists();
    return false;
    }
    });

    // 결과
    내
    재검색 - 검색
    버튼
    클릭시
    $('#conts .re_serch').on('click', '.fl_left button', function()
    {
        searchArtists();
    return false;
    });

    // 정렬
    클릭시
    $('#conts .re_serch').on('click', '.list_sort [data-sort]', function()
    {
    $('#conts .re_serch .list_sort [data-sort].on').removeClass('on');
    $(this).addClass('on');

    searchArtists();
    return false;
    });

    });
    < / script >
        <!-- // contents -->
    < / div >
        < / div >
            <!-- footer -->
    < div
    id = "footer" >
         < div


    class ="btn_top_wrap" >

    < a


    class ="btn_top" href="#skip_nav" style="" title="맨 위로 가기" > < span > 맨 위로 가기 < / span > < / a >

    < / div >
    < div


    class ="wrap_pop_notice" id="popNotice" >

    < div


    class ="pop_notice_inner" >

    < div


    class ="bd" >

    < h1 > 웹
    브라우저
    보안
    암호화 < br / > 알고리즘
    업그레이드
    안내 < / h1 >
    < div


    class ="wrap_notice" >

    < div


    class ="info_cont" >

    < div


    class ="txt01" >

    < p > 안녕하세요.보안
    암호화
    알고리즘
    업그레이드
    관련
    멜론에서
    알려드립니다. < br / > 지금
    이용하고
    계신
    OS와
    브라우저는
    새로운
    보안
    암호화
    알고리즘을
    지원하 < br / > 지
    못하여
    이용이
    제한
    될
    수
    있습니다 < / p >
    < p


    class ="pgh" > 현재 적용된 SHA-1 보안 암호화 알고리즘은 데이터 위조공격 가능성이 있어 < br / > 주요 브라우저들의 지원 중단이 예정되어있습니다.< br / > 멜론에서도 회원 분들의 좀 더 안전한 서비스 이용을 보장하기 위해 보안 암호 < br / > 화 알고리즘 업그레이드를 진행 할 예정입니다.< / p >

    < / div >
    < div


    class ="txt02" >

    < p > 업그레이드
    내용: SHA - 1
    방식 → SHA - 2
    방식으로
    업그레이드 < / p >
    < p


    class ="date" > 적용일: <


        span > 2016
    년
    12
    월
    23
    일 < / span > < / p >
    < / div >
    < / div >
    < div


    class ="info_cont cont2" >

    < div


    class ="txt01" >

    < p > 보안
    암호화
    알고리즘
    업그레이드에
    따라
    SHA - 2
    방식을
    지원하지
    않는
    OS나 < br / > 브라우저를
    이용하시면
    멜론서비스
    이용에
    제한이
    있을
    수
    있습니다. < br / > 아래
    지원
    가능한
    OS
    또는
    브라우저를
    확인하시고
    회원
    분들께서는
    업데이트 < br / > 후
    이용해주시기
    바랍니다. < / p >
    < / div >
    < div


    class ="txt02" >

    < dl >
    < dt > SHA - 2
    지원
    OS / 브라우저 < / dt >
    < dd >
    < p > OS < / p >
    < ul >
    < li > Windows
    XP
    SP3
    이상 < / li >
    < li > Mac
    OS
    X
    10.5
    이상 < / li >
    < / ul >
    < / dd >
    < dd


    class ="list" >

    < p > 브라우저 < / p >
    < ul >
    < li > Internet
    Explorer
    버전
    7
    이상 < / li >
    < li > Chrome
    버전
    26
    이상 < / li >
    < li > FireFox: 버전
    1.5
    이상 < / li >
    < li > Safari: 버전
    3
    이상(Mac
    OS
    X
    10.5
    이상) < / li >
    < li > Opera: 버전
    7
    이상 < / li >
    < / ul >
    < / dd >
    < / dl >
    < p


    class ="refer" > * 멜론서비스는 공식적으로 IE8이상 지원하며, Opera는 미지원함을 참고 부탁드립니다.< / p >

    < / div >
    < div


    class ="txt03" >

    < p > 앞으로도
    좋은
    서비스와
    안정성으로
    보답할
    수
    있도록
    최선을
    다하겠습니다. < br / > 감사합니다. < / p >
    < / div >
    < / div >
    < / div >
    < div


    class ="wrap_input_box" >

    < div


    class ="check_area d_check_on" >

    < input
    data - cookie - id = "popNotice"
    id = "todayChk"
    type = "checkbox" / >
    < label
    for ="todayChk" > 오늘하루 보지 않기 < / label >
    < / div >
    < div


    class ="btn-area" >

    < button


    class ="d_close" type="button" > < span > 확인 < / span > < / button >

    < / div >
    < / div >
    < / div >
    < / div >
    < span


    class ="shadow" > < / span >

    < / div >
    < div


    class ="footer_cont" >

    < div


    class ="footer_menu" >

    < !-- < ul


    class ="fl_left" > -->

    < !-- < li


    class ="menu01 d_melon_ticket" > < a href="http://ticket.melon.com/main/index.htm" > < span > MelOn Ticket < / span > < / a > < / li > -->

    < !-- < li


    class ="menu04" > < a href="http://aztweb.melon.com/aztalk/guide/web/main.htm" > < span > aztalk < / span > < / a > < / li > -->

    < !-- < / ul > -->
    < ul


    class ="fl_right" >

    < li


    class ="menu05" > < a href="http://www.melon.com/serviceintro/index.htm" > < span > 멜론4.0 둘러보기 < / span > < / a > < / li > < !-- 160824 수정 -->

    < li


    class ="menu06" > < a href="http://www.melon.com/customer/serviceintro/index.htm" > < span > Windows 플레이어 < / span > < / a > < / li > < !-- 160824 수정 -->

    < li


    class ="menu07" > < a href="http://www.melon.com/customer/serviceintro/multi_pc_web.htm" > < span > Mac 플레이어 < / span > < / a > < / li >

    < li


    class ="menu09" > < a href="http://www.melon.com/customer/serviceintro/ipad.htm" > < span > iPad < / span > < span class ="icon_new" > < / span > < / a > < / li >

    < li


    class ="menu08" > < a href="http://faqs2.melon.com/customer/index.htm" > < span > 고객센터 < / span > < / a > < / li >

    < / ul >
    < / div >
    < ul


    class ="footer_policy clfix" >

    < li


    class ="first_child" > < a href="http://www.iloen.com/" target="_blank" title="회사소개 " > 회사소개 < / a > < / li >

    < li > < a
    href = "http://info.melon.com/terms/web/terms1_1.html"
    target = "_blank"
    title = "이용약관 " > 이용약관 < / a > < / li >
    < li > < a
    href = "http://info.melon.com/terms/web/terms3.html"
    target = "_blank"
    title = "개인정보처리방침 " > < strong > 개인정보처리방침 < / strong > < / a > < / li >
    < li > < a
    href = "http://info.melon.com/terms/web/terms5_1.html"
    target = "_blank"
    title = "청소년보호정책" > 청소년보호정책 < / a > < / li >
    < li > < a
    href = "http://faqs2.melon.com/customer/faq/informFaq.htm?no=1&amp;faqId=QUES20140616000001&amp;SEARCH_KEY=&amp;SEARCH_PAR_CATEGORY=CATE20130909000006&amp;SEARCH_CATEGORY=CATE20130909000021"
    title = "제휴/프로모션문의" > 제휴 / 프로모션문의 < / a > < / li >
    < li > < a
    href = "javascript:openEmailCollectionReject();"
    title = "이메일주소무단수집거부 " > 이메일주소무단수집거부 < / a > < / li >
    < li > < a
    href = "https://partner.melon.com/partrct/login/web/login_loginProcess.htm?t=s"
    target = "_blank"
    title = "파트너센터" > 파트너센터 < / a > < / li >
    < li


    class ="last_child" > < a href="http://www.ftc.go.kr/info/bizinfo/communicationView.jsp?apv_perm_no=2011322016230202008&amp;area1=&amp;area2=&amp;currpage=2&amp;searchKey=01&amp;searchVal=로엔&amp;stdate=&amp;endate=" title="사업자정보확인" > 사업자정보확인 < / a > < / li > < !-- 160629 추가 -->

    < / ul >
    < !--160531
    수정
    lyr -->
    < p >
    < span


    class ="first" > 서울시 강남구 테헤란로 103길 17 < / span > < span > 대표이사: 박성훈 <

    / span > < span > 사업자등록번호: 138 - 81 - 05
    876 < / span > < span > 통신판매업
    신고번호: 제2011 - 서울강남 - 0200
    8
    호 < / span > < br / > < span


    class ="first" > 문의전화(평일 09:00


    ~18: 00): 1566 - 7727(유료) < / span > < span > 이메일: < a


    class ="btn_footer_mail" href="https://help.melon.com/web/customer/help/helpForm.htm?type=" target="_blank" > meloninformation @ iloen.com < / a > < / span > < span > © 2016. LOEN Entertainment, Inc.ALL RIGHTS RESERVED.< / span >

    < / p >
    < !-- // 160531
    수정
    lyr -->
    < !--161209
    수정
    lyr -->
    < div


    class ="ban" >

    < a
    href = "http://www.melon.com/footer/awrad.htm?pageType=02" > < img
    alt = "2017 대한민국 퍼스트브랜드 대상"
    height = "25"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer01_170110.png"
    width = "100" / > < / a >
    < a
    href = "http://www.melon.com/footer/awrad.htm?pageType=04" > < img
    alt = "2017 소비자가 뽑은 가장 신뢰하는 브랜드 대상"
    height = "25"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer04_170110.png"
    width = "125" / > < / a >
    < a
    href = "http://www.melon.com/footer/awrad.htm?pageType=03" > < img
    alt = "한국능률협회컨설팅 2017 브랜드 파워 1위"
    height = "25"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer02_170308.png"
    width = "113" / > < / a >
    < a
    href = "http://www.melon.com/footer/awrad.htm?pageType=05" > < img
    alt = "2016 대한민국 브랜드 고객충성도 1위"
    height = "25"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer10.png"
    width = "118" / > < / a >
    < a
    href = "http://www.kdce.or.kr/user/ctf/clmsCtfTransList.do?NmberBusiRegNo=1388105876&amp;websiteName=www.melon.com&amp;SUB=FB"
    target = "_blank" > < img
    alt = "음악저작권 이용허락 인증"
    height = "25"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer06_161209.png"
    width = "82" / > < / a >
    < a
    href = "http://www.cleansite.org/"
    target = "_blank" > < img
    alt = "클린사이트"
    height = "25"
    src = "http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer07_161209.png"
    width = "70" / > < / a >
    < a


    class ="last_child" href="http://isms.kisa.or.kr/" target="_blank" > < img alt="정보보호 관리체계 ISMS 인증" height="25" src="http://cdnimg.melon.co.kr/resource/image/web/common/ban_footer09_161209.png" width="102" / > < / a >

    < / div >
    < !-- // 161209
    수정
    lyr -->
    < !--모바일
    웹
    버전, 태블릿에서만
    적용됨.display
    none, block
    으로
    적용 -->
    < !--140602
    추가
    lyr -->
    < div


    class ="mobile_btn_wrap" style="display:none;" >

    < p > 접속하신
    단말 / 브라우저에서는
    멜론
    서비스의
    사용이
    일부
    제한될
    수
    있습니다.양해부탁드립니다. < / p >
    < a


    class ="btn" href="#" title="모바일 웹 버전" >

    < span


    class ="odd_span" >

    < span


    class ="even_span" > 모바일 웹 버전 < / span >

    < / span >
    < / a >
    < / div >
    < !-- // 140602
    추가
    lyr -->
    < / div >
    < a


    class ="btn_top" href="#" style="display: none;" title="맨 위로 가기" > 맨 위로 가기 < / a >

    < script
    type = "text/javascript" >

    $(function() {
    // favicon 분기 처리
    var pocId = MELON.WEBSVC.POC.getPocId();
    if ('AS20' == pocId | | 'HT10' == pocId){
    $('link#favicon').attr('href', 'http://cdnimg.melon.co.kr/resource/mobile40/cds/common/image/favicon.ico');
$('title').text('Melon');
} else if ('IS20' == pocId | | 'IT10' == pocId){
$('link#favicon').attr('type', '');
$('link#favicon').attr('rel', 'apple-touch-icon-precomposed');
$('link#favicon').attr('href', 'http://cdnimg.melon.co.kr/resource/mobile40/cds/common/image/mobile_apple_120x120.png');
$('link#favicon').after('<link rel="apple-touch-icon-precomposed" sizes="180x180" href="http://cdnimg.melon.co.kr/resource/mobile40/cds/common/image/mobile_apple_180x180.png" />');
$('title').text('Melon');
}

// 모바일(t.com)에서 넘어온 경우 - 모바일(t.com) 서비스 종료로 삭제
/ *
var fromMobileWeb = getCookie("D");

    if (fromMobileWeb != null & & fromMobileWeb.indexOf('T') > -1){
    $("#btnMobileWeb").css("display", "block");
    }
    * /
    // 엣지 브라우저이고 해당 팝업이 뜬 적이 없는 경우 체크하여 팝업을 띄운다.
    var isEdge = (navigator.userAgent.indexOf("Edge") > 0);
    var edgeCheckYN = getCookie("EDGE_CHECK") != 'Y';

    if (isEdge & & edgeCheckYN){
    window.open('http://www.melon.com/error_page/error_edgeTypeA.html', 'edgeCheck', 'scrollbars=no, resizable=no, location=no, width=560, height=498');
    }

    // 타블렛이고 해당 팝업이 뜬 적이 없는 경우 체크하여 팝업을 띄운다.
    var tabletCheckYN = getCookie("TABLET_CHECK") != 'Y';

    if (melon.isTablet() & & tabletCheckYN){
    window.open('http://www.melon.com/error_page/error_tabletTypeA.html', 'tabletPopTypeA', 'scrollbars=no, resizable=no, location=no, width=560, height=483');
    }

    // 해당 쿠키가 존재하면 쿠키 삭제
    if (getCookie("CHECK_POP") != ''){
    // 체크 후 해당 쿠키는 제거
    var expireDate = new Date();
    expireDate.setDate(expireDate.getDate()-1);
    document.cookie = "CHECK_POP=;path=/;expires="+expireDate.toGMTString()+";domain=.melon.com";
    }

    if (isMelonLogin()){
    var djYn = getMemberDjYn();
    if (djYn == "" | | typeof djYn == "undefined"){
    try {
    $.ajax({
    url: "http://www.melon.com/gnb/check_melondj.json",
         type: 'GET',
    dataType: 'jsonp',
    jsonp: 'jscallback',
    }).done(function(json)
    {}).fail(function()
    {});
    } catch(e)
    {}
    }
    }

    // 홈탭의
    경우
    쇼핑 / 티켓을
    새창띄우기로
    변경한다.
        var
    fromMPS = getCookie("MPS"); // 멜론
    플레이어에서
    왔는지
    확인.
        var
    fromHomeTab = !(fromMPS == null | | fromMPS.indexOf("MELONPLAYER") < 0);

    if (fromHomeTab){
    $("li.d_melon_shopping a").removeClass("mlog");
    $("li.d_melon_shopping a").addClass("mlog_without_page_change");
    $("li.d_melon_shopping a").attr("target", "_blank");

    $("li.d_melon_ticket a").removeClass("mlog");
    $("li.d_melon_ticket a").addClass("mlog_without_page_change");
    $("li.d_melon_ticket a").attr("target", "_blank");
    }

    // SHA-2 popup
    function uaChecker() {
    var r = true;
    var uav = navigator.userAgent.replace( / / g, '');
    var exUA =['OSX10_1_', 'OSX10_2_', 'OSX10_3_', 'OSX10_4_', 'OSX10.1.', 'OSX10.2.', 'OSX10.3.', 'OSX10.4.',
    'Windows95', 'Windows98', 'WindowsNT4.0', 'WindowsNT5.0', 'MSIE6'];
    $.each(exUA, function(i, v)
    {
    if (uav.indexOf(v) > -1)
    {
        r = false;
    }
    });
    if (uav.indexOf("WindowsNT5.1") > -1 & & uav.indexOf("SV1") > -1) {
    r = false;
    }
    var
    chp = uav.indexOf("Chrome");
    if (chp > -1){if ( parseInt(uav.substr(chp + 7, 3)) < 26 ) {r = false;}}
    if (chp == -1 & & uav.indexOf("Safari") > -1) {if ( parseInt(uav.substr(uav.indexOf("Version") + 8, 3)) < 3 ) {r = false;}}
    if (uav.indexOf("Firefox") > -1) {if ( parseFloat(uav.substr(uav.indexOf("Firefox") + 8, 3)) < 2 ) {r = false;}}
    if (uav.indexOf("OPR/") > -1 | | uav.indexOf("Opera/") > -1) {
    var
    fv = 0;
    if (uav.indexOf("OPR/") > -1) {fv = parseFloat(uav.substr(uav.indexOf("OPR/") + 4, 3));}
    else if ( uav.indexOf("Opera/") > -1 ) {fv = parseFloat(uav.substr(uav.indexOf("Opera/") + 6, 3));}
    if (fv < 7) {r = false;}
    }
    return r;
    }

    // 웹
    브라우저
    보안
    암호화
    161121
    $('.d_check_on').on('click', 'label', function()
    {
    if ($(this).siblings('input').prop('checked')) {
    $(this).parents('.d_check_on').removeClass('on');
    } else {
    $(this).parents('.d_check_on').addClass('on');
    };
    });
    $(document).on('limitpopup', function(e, cookieId)
    {
    if (!uaChecker() ) {
    $('#' + cookieId).modal();
    }
    });
    setTimeout(function()
    {
    $("#popNotice").timeLimitSet({cookieId: 'popNotice', selectors: {closebtn: '#todayChk', checkbox: ''}});
    }, 1);
    MELON.PBPGN.TimeLimitPopup.init({cookieId: "popNotice", serverTime: new Date(), limitType: "day"});
    $("#popNotice .d_close").click(function()
    {  $("#popNotice").modal('hide');});
    });

    function
    goMelonTPage()
    {
    // 쿠키
    삭제
    후
    t.com으로
    페이지
    이동
    var
    expireDate = new
    Date();
    expireDate.setDate(expireDate.getDate() - 1);
    document.cookie = "D=;path=/;expires=" + expireDate.toGMTString() + ";domain=.melon.com";

    location.href = 'http://t.melon.com';
    }

    function
    openEmailCollectionReject()
    {
        window.open('http://www.melon.com/emailCollectionReject.html', 'emailCollect',
                    'scrollbars=no, resizable=no, location=no, width=384, height=331');
    }

    // 다음
    검색
    랜딩
    추가
    if (location.href.indexOf('ref=W10600') > -1)
    {
    $.ajax({
    url: '/gnb/daumsearch_list.htm',
    }).done(function(html)
    {
    $('#footer').before(html);
    });
    }

    < / script >
        <!-- // 140602
    추가
    lyr -->
    < / div >
        <!-- // footer -->
    < / div >
        < style
    type = "text/css" >
    .ui - helper - hidden - accessible
    {border: 0;
    clip: rect(0
    0
    0
    0); height: 1
    px;
    margin: -1
    px;
    overflow: hidden;
    padding: 0;
    position: absolute;
    width: 1
    px;}

    # wrap.search .auto_complete .text_result > li { height:inherit; margin:0; padding:0; }
    # wrap.search .auto_complete .text_result > li:hover { background:none; }
    # wrap.search .auto_complete .text_result > li.result_none { height:18px; padding:4px 0 0 11px; margin:8px 5px 0 1px; }
    # wrap.search .auto_complete .text_result > li a { display:block; max-width:419px; height:18px; padding:4px 0 0 11px; margin:0 5px 0 1px; text-decoration:none;}

    # wrap.search .auto_complete li > a.ui-state-focus,
    # wrap.search .auto_complete li > a.ui-state-active { background:#f5f5f5; }
    # wrap.search .auto_complete b {color:#739900;}
    < / style >
        < / body >
            < / html >