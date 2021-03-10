from django.test import TestCase
from student.models import Student
import json

BOY_NAMES = ["邱项明", "顾俊悟", "王弘毅", "杜烨煜", "钱锐智", "戴飞语", "吴阳州", "田雅珺", "陆德本", "谭俊爽",
             "梁星驰", "薛兴修", "黄理群", "吕英悟", "金旭尧", "顾英卫", "毛茂典", "邓宜民", "龙玉宇", "曾鹏翼",
             "王旭尧", "金志泽", "程文虹", "韩力勤", "曾星晖", "邱欣然", "易高岑", "冯永丰", "林奇胜", "阎永长",
             "钟高杰", "刘高爽", "钱景铄", "谭成荫", "曾雅懿", "邱康盛", "陆新霁", "郑恺歌", "侯鸿卓", "于和顺",
             "陈高朗", "林飞昂", "胡璞玉", "潘建弼", "黎天干", "侯嘉祯", "冯信然", "苏良骥", "熊勇军", "李同化",
             "任鸿禧", "谢高卓", "韩鸿振", "傅和宜", "王昊天", "石天和", "胡和硕", "邹英飙", "邵丰茂", "曹勇锐",
             "吕英光", "郝子晋", "胡志文", "罗修齐", "董成龙", "崔烨烁", "姜光亮", "唐鸿福", "潘斌蔚", "侯经纶",
             "吴博明", "汪昊昊", "易奇正", "黄兴国", "石景胜", "顾星光", "夏明亮", "阎英睿", "黄宇文", "熊建树",
             "贺澔", "康心", "阎馗", "丁士", "吕僳", "常葆", "李瑎", "白丞", "周俯", "孟健"]
GIRL_NAMES = ["江布侬", "钟盼曼", "苏瑜敏", "侯曼云", "谢思云", "张尤文", "沈歆琳", "侯思艳", "崔施诗", "赖易梦",
              "许淑贞", "秦忻然", "史小楠", "苏润丽", "江觅柔", "方运菱", "朱韵诗", "万从菡", "贾怜菡", "尹苏弥",
              "韩明艳", "丁安茹", "贾望雅", "薛秋灵", "张嘉洁", "周雅霜", "陆李媛", "沈春雁", "马思恩", "郭若灵",
              "李淑穆", "田丝琦", "孙洮洮", "萧云亭", "杨含雁", "戴瑶华", "方和煦", "蔡子婧", "许绮玉", "邵嘉云",
              "周睿瑶", "董子怡", "谢小萱", "高修美", "方书蕾", "廖莉娅", "韩兰娟", "贾柔谨", "吕映之", "孟芬馥",
              "金芳懿", "袁靖儿", "高紫颖", "余悦宜", "郭彦慧", "卢继红", "侯宜楠", "范丹溪", "梁瑜英", "朱梓洁",
              "廖翠绿", "吕饮香", "陈歌阑", "周怀柔", "许兰若", "尹恬美", "胡梧桐", "余霁芸", "叶尔云", "丁翠岚",
              "孙岚岚", "吴佩珍", "苏蝾婷", "钟诗蕾", "王安妮", "李夏璇", "谢会雯", "姜展文", "黄寻桃", "姚晓丝",
              "黄娘", "董丽", "黄美", "江霓", "杜滢", "钟影", "潘惠", "文悦", "萧茹", "郝雯"]


def query_from_db(model_name, filter_params):
    queryset = model_name.objects.filter(gender=filter_params)
    data = queryset.values()

    return list(data)


class StudentTest(TestCase):

    def setUp(self):
        for boy, girl in zip(BOY_NAMES, GIRL_NAMES):
            Student.objects.create(name=boy, gender=1)
            Student.objects.create(name=girl, gender=0)

    def test_get_student_by_gender(self):
        for _ in [0, 1]:
            response = self.client.get('/students/?gender={}'.format(_))
            self.assertEqual(response.status_code, 200)

            res = query_from_db(Student, _)
            self.assertEqual(json.loads(response.content).get("data"), res)
