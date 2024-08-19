from django.shortcuts import render

from .models import NaverNews
# Create your views here.

from django.core.paginator import Paginator



def news_search(request):
    naver_news = NaverNews.objects.all()

    mode = request.GET.get('mode')
    keyword = request.GET.get('keyword')
    print('mode=[%s], keyword=[%s]' % (mode, keyword))

    if mode and keyword:
        if mode == 'title':
            naver_news = naver_news.filter(title__icontains=keyword)
        elif mode == 'section':
            naver_news = naver_news.filter(section__icontains=keyword)

    pageSize = 10
    paginator = Paginator(naver_news, pageSize)

    pageNumber = request.GET.get('page')
    naver_newsList = paginator.get_page(pageNumber)

    pageCount = 10
    totalPage = paginator.num_pages

    if pageNumber == None:  # 처음 시작 되었을 때
        pageNumber = 1
        beginPage = 1
        endPage = 10

    else:
        print('pageNumber=' + pageNumber)
        pageNumber = int(pageNumber)
        beginPage = (pageNumber -1) // pageSize*pageSize + 1
        endPage =  beginPage + pageCount - 1

        if(totalPage < endPage):
            endPage = totalPage
    #end if

    has_previous = pageNumber > pageCount
    print('has_previous=' + str(has_previous))

    has_next = pageNumber < (totalPage // pageCount * pageCount + 1)
    print('has_next=' + str(has_next))

    print('beginPage=' + str(beginPage))
    print('endPage=' + str(endPage))
    # Template(html 문서) 파일에서는 range()를 사용할 수 없다
    page_range = range(int(beginPage), int(endPage) + 1)

    # 페이지로 넘어 오는 파라미터 정보
    query_params = request.GET.copy()

    # page 파라미터를 제거한 다음 쿼리 문자열을 전송하도록 합니다.
    delete_param = 'page'

    if 'page' in query_params:
        del query_params[delete_param]

    # 넘겨진 쿼리 목록의 문자열 집합을 QueryString이라고 부릅니다.
    query_params = query_params.urlencode()
    print('query__paras=[' + str(query_params) + ']')

    context = {'naver_newsList': naver_newsList, 'beginPage': beginPage, 'endPage': endPage, 'page_range': page_range,
               'has_previous': has_previous, 'has_next': has_next, 'query_params': query_params,
               'pageNumber': pageNumber, 'totalPage': totalPage}

    return render(request, 'nndb/news_search.html', context)
# den def