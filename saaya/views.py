from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .logics import getExternalResults
from portfolio.seoclass import SEOClass

def saayaIndex(request):
    tags = SEOClass(
        title= "Saaya: An Autocomplete assistant",
        description= "Saaya is an autocomplete tool which fetches data from popular search engines and display them to you on a single page.",
        keywords= "Saaya, Google Autocomplete, Bing Autocomplete, DuckDuckGo Autocomplete, Autocomplete, Autocomplete assistant. Search Engine, Autosuggest",
    )

    meta_tags = tags.get_meta_tags()
    og_tags = tags.get_open_graph_tags()
    return render(request, "saaya/index.html", {
        "meta_tags": meta_tags,
        "og_tags": og_tags,
    })

# until asyncio is fixed in python 3.12
@require_POST
def getResults(request):
    query = request.POST.get("query")
    result = getExternalResults(query)
    if result:
        google_out = ''.join(f'<li class="list-item">{i}</li>' for i in result[0])
        bing_out = ''.join(f'<li class="list-item">{i}</li>' for i in result[1])
        ddg_out =  ''.join(f'<li class="list-item">{i}</li>' for i in result[2])
        return HttpResponse(

            f'''

        <div id="resultsdiv" class="grid grid-cols-1 gap-3 md:grid-cols-3 mx-auto px-1 max-w-7xl">
                    <div class="card" id="scrlto">
                    <div class="card-header font-bold">Google</div>
                    <div class="card-body">
                    <ul class="list list-flush">
                        {google_out}
                    </ul>
                    </div>
                    </div>
                    <div class="card">
                    <div class="card-header font-bold">Bing</div>
                    <div class="card-body">
                        <ul class="list list-flush">
                        {bing_out}
                        </ul>
                    </div>
                </div>
                    <div class="card">
                    <div class="card-header font-bold">DuckDuckGo</div>
                    <div class="card-body">
                        <ul class="list list-flush">
                        {ddg_out}
                        </ul>
                    </div>
                </div>
                </div>
    '''
        )
    else:
        return HttpResponse('''  <div class="alert text-red-700 bg-red-100 mx-1 md:mx-auto max-w-3xl " role="alert">Your request can't be completed right now. Please try again.</div> ''')
# @require_POST
# async def getResults(request):
#     query = request.POST.get("query")
#     result = await getExternalResults(query)
#     if result:
#         google_out = ''.join(f'<li class="list-item">{i}</li>' for i in result[0])
#         bing_out = ''.join(f'<li class="list-item">{i}</li>' for i in result[1])
#         ddg_out =  ''.join(f'<li class="list-item">{i}</li>' for i in result[2])
#         return HttpResponse(

#             f'''

#         <div id="resultsdiv" class="grid grid-cols-1 gap-3 md:grid-cols-3 mx-auto px-1 max-w-7xl">
#                     <div class="card" id="scrlto">
#                     <div class="card-header font-bold">Google</div>
#                     <div class="card-body">
#                     <ul class="list list-flush">
#                         {google_out}
#                     </ul>
#                     </div>
#                     </div>
#                     <div class="card">
#                     <div class="card-header font-bold">Bing</div>
#                     <div class="card-body">
#                         <ul class="list list-flush">
#                         {bing_out}
#                         </ul>
#                     </div>
#                 </div>
#                     <div class="card">
#                     <div class="card-header font-bold">DuckDuckGo</div>
#                     <div class="card-body">
#                         <ul class="list list-flush">
#                         {ddg_out}
#                         </ul>
#                     </div>
#                 </div>
#                 </div>
#     '''
#         )
#     else:
#         return HttpResponse('''  <div class="alert text-red-700 bg-red-100 mx-1 md:mx-auto max-w-3xl " role="alert">Your request can't be completed right now. Please try again.</div> ''')