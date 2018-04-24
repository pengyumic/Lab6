import requests
from lxml import html
import re


class course:

    def __init__(self, title=None, info=None, seats=None, url=None):
        self.course_title = title
        self.course_info = info
        self.course_seats = seats
        self.course_url = url
        self.course_crn = None
        if url != None:
            self.course_crn = re.search('crn_in=(\d+)', url).group(1)


    def set_info(self, info):
        self.course_info = info


    def set_seats(self, seats):
        self.course_seats = seats


    def set_url(self, url):
        self.course_url = url
        self.course_crn = re.search('crn_in=(\d+)', url).group(1)

    def is_available(self):
        return int(self.course_seats['Remaining'][0]) > 0

    def email_format(self):
        return self.course_title+" now has "+self.course_seats['Remaining'][0]+" remaining seats"
    def __str__(self):
        return self.course_title+"\n"+str(self.course_seats)+"\n"\
            +str(self.course_seats)+"\n"+self.course_url+"\n"\
            +str(self.course_crn)

class search:

    def __init__(self):
        self.domain = 'https://selfservice.mypurdue.purdue.edu'

    def get_courses(self, form):
        courses = self.find_urls(form)
        self.get_tables(courses)
        return courses


    def find_urls(self, form):
        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Length':'411',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'selfservice.mypurdue.purdue.edu',
            'Origin':'https://selfservice.mypurdue.purdue.edu',
            'Pragma':'no-cache',
            'Referer':'https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_cat_term_date',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }
        url = 'https://selfservice.mypurdue.purdue.edu/prod/bwckschd.p_get_crse_unsec'
        r = requests.post(url, headers=header, data=form)
        tree = html.fromstring(r.text)
        sections = tree.xpath('//th[@class="ddlabel"]/a/text()')
        ddlabel = tree.xpath('//th[@class="ddlabel"]')
        titles = [i.getchildren()[0].xpath("text()")[0] for i in ddlabel]
        section_urls = [i.getchildren()[0].xpath("@href")[0] for i in ddlabel]
        tables = tree.xpath('//table[@summary="This table lists the scheduled meeting times and assigned instructors for this class.."]')
        ddheaders = [tables[i].xpath("tr/th/text()") for i in range(len(tables))]
        # for regex pattern matching
        pattern = '[ \t\\w:-]+'
        rows = [[s for (i, s) in enumerate([i.group(0) for i in [re.search(pattern, i) for i in tables[j].xpath('tr[position()>1]//text()')] if i!= None]) if (i+1)%8] for j in range(len(tables))]
        courses = [course(title=titles[i], info=dict(zip(ddheaders[i], rows[i])), url=self.domain+section_urls[i]) for i in range(len(ddheaders))]
        return courses

    def get_tables(self, courses):
        has_seats = []
        for k in range(len(courses)):
            header1 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Host': 'selfservice.mypurdue.purdue.edu',
                'Origin': 'https://selfservice.mypurdue.purdue.edu',
                'Pragma': 'no-cache',
                'Referer': 'https://selfservice.mypurdue.purdue.edu/prod/bwckschd.p_get_crse_unsec',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
            tree = html.fromstring(requests.get(courses[k].course_url, headers=header1, allow_redirects=False).text)
            table = tree.xpath('//table[@class="datadisplaytable"]')[1]
            rs = table.findall('tr')

            nums = [rs[i].xpath('th[@class="ddlabel"]/span/text()|td[@class="dddefault"]/text()') for i in range(1, len(rs))]
            s = []
            for i in range(len(nums[0])):
                t = []
                for j in range(len(nums)):
                    t.append(nums[j][i])
                s.append(t)
            seats = dict(zip([i.xpath('text()')[0] if i.get('class') == 'dddead' else i.xpath('span/text()')[0] for i in rs[0].getchildren()], s))
            courses[k].set_seats(seats)
            if courses[k].is_available():
                has_seats.append(k)
        return has_seats
