# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mockJobDatabase.settings')

# import django
# django.setup()

# # Populating script
# import random
# from apiDatabase.models import Topic, Webpage, AccessRecords
# from faker import Faker

# fakegen = Faker()
# topics = ['Search', 'Social', 'Marketplace', 'News']

# def add_topic():
# 	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
# 	t.save()
# 	return t

# def populate(N):
	


# # # from apiDatabase.models import City, Languages, AccessCounts
# # # from apiDatabase.models import City, Languages
# # from random import seed
# # from random import randint

# # seed(1)
# # cities = ["New York", "San Francisco", "Boston", "Austin", "Chicago"]

# # def add_cities():
# # 	c = City.objects.get_or_create(city_name=random.choice(cities))[0]
# # 	c.save()
# # 	return c

# # def populateLanguageCount(N=10):
# # 	for entry in range(N):
# # 		city = add_cities()
# # 		c = City.objects.get_or_create(city_name=random.choice(cities))[0]
# # 		c.save()

# # 		# create fake data
# # 		c = randint(0, 10)
# # 		c_plus = randint(0, 10) # C++
# # 		c_sharp = randint(0, 10) # C#
# # 		dart = randint(0, 10)
# # 		go = randint(0, 10)
# # 		haskell = randint(0, 10)
# # 		html_css = randint(0, 10)
# # 		java = randint(0, 10)
# # 		javaScript = randint(0, 10)
# # 		kotlin = randint(0, 10)
# # 		matLab = randint(0, 10)
# # 		obj_c = randint(0, 10)
# # 		perl = randint(0, 10)
# # 		php = randint(0, 10)
# # 		python = randint(0, 10)
# # 		r = randint(0, 10)
# # 		ruby = randint(0, 10)
# # 		rust = randint(0, 10)
# # 		scala = randint(0, 10)
# # 		swift = randint(0, 10)
# # 		typeScript = randint(0, 10)
# # 		visual_basic = randint(0, 10)
# # 		asp_net = randint(0, 10)
# # 		angular = randint(0, 10)
# # 		bootstrap = randint(0, 10)
# # 		django = randint(0, 10)
# # 		ember = randint(0, 10)
# # 		flask =randint(0, 10)
# # 		laravel = randint(0, 10)
# # 		node_js = randint(0, 10)
# # 		rails = randint(0, 10)
# # 		react = randint(0, 10)
# # 		spring = randint(0, 10)
# # 		vue_js = randint(0, 10)
# # 		ms_sql = randint(0, 10) # ms sql server
# # 		mongoDB = randint(0, 10)
# # 		my_sql = randint(0, 10)
# # 		postGreSql = randint(0, 10)
# # 		redis = randint(0, 10)
# # 		sqlite = randint(0, 10)

# # 		languageForCity = Languages.objects.get_or_create(city=city, c=c)[0]
# # 		#.save()

# # def main():
# # 	print("YOOOOOOOOOOOO")
# # 	print('populating')
# # 	# populateLanguageCount(10)
# # 	print('done')

# # if __name__== 'main':
# # 	main()





import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mockJobDatabase.settings')

import django
django.setup()

## FAKE POPULATION script
import random
from apiDatabase.models import City, Languages
import urllib.request
import json
import random
import requests

city = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'San Diego','Ann Arbor', 'San Francisco',
 'San Jose', 'Seattle', 'Sacramento', 'San Antonio', 'Riverside', 'Raleigh', 'Pittsburgh',
 'Philadelphia', 'Orlando', 'New York City', 'Minneapolis', 'Miami', 'Madison', 'Los Angeles', 'Las Vegas', 'Ithaca',
 'Houston', 'Fort Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville',
 'Charlotte', 'Boulder', 'Baltimore', 'Austin']

# def add_city(num):
# 	c = City.objects.get_or_create(city_name = city[num])[0] #tuple returns objects
# 	c.save()
# 	return c

# def random_int():
# 	fake_num = fakegen.random_int(0, 100)
# 	return fake_num

def getGitHubResponse(url):
	operUrl = urllib.request.urlopen(url)
	if(operUrl.getcode()==200):
		data = operUrl.read()
		jsonData = json.loads(data)
	else:
		print("Error receiving data", operUrl.getcode())
	return jsonData

def get_language_count(city_url, lang_search):
	city_language_url = city_url + lang_search
	try:
		tech_response = getGitHubResponse(city_language_url)
		lang_count = len(tech_response)
	except:
		return -1
	return lang_count


def populate():
	city_array_actual = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'San Diego','Ann Arbor', 'San Francisco', 'Jose', 'Seattle', 'Sacramento', 'San Antonio', 'Riverside', 'Raleigh', 'Pittsburgh','Philadelphia', 'Orlando', 'New York City', 'Minneapolis', 'Miami', 'Madison', 'Los Angeles', 'Las Vegas', 'Ithaca','Houston', 'Fort Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville','Charlotte', 'Boulder', 'Baltimore', 'Austin']
	city_array_search = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'Diego','Ann Arbor', 'Francisco', 'Jose', 'Seattle', 'Sacramento', 'Antonio', 'Riverside', 'Raleigh', 'Pittsburgh','Philadelphia', 'Orlando', 'NYC', 'Minneapolis', 'Miami', 'Madison', 'Angeles', 'Vegas', 'Ithaca','Houston', 'Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville','Charlotte', 'Boulder', 'Baltimore', 'Austin']

	for c in range(len(city_array_search)):
		city = City.objects.get_or_create(city_name = city_array_actual[c])[0]
		city.save()
	
		city_url = "https://jobs.github.com/positions.json?location=" + city_array_search[c]
		try:
			fake_c = get_language_count(city_url, "&search=c")
			print(fake_c)
			fake_cplus = get_language_count(city_url, "&search=c++")
			fake_csharp = get_language_count(city_url, "&search=c#")
			fake_dart = get_language_count(city_url, "&search=dart")
			fake_go = get_language_count(city_url, "&search=go")
			fake_haskell = get_language_count(city_url, "&search=haskell")
			fake_html = get_language_count(city_url, "&search=html")
			fake_java = get_language_count(city_url, "&search=java")
			fake_javascript = get_language_count(city_url, "&search=javascript")
			fake_kotlin = get_language_count(city_url, "&search=kotlin")
			fake_matLab = get_language_count(city_url, "&search=matlab")
			fake_obj_c  = get_language_count(city_url, "&search=objective")
			fake_perl  = get_language_count(city_url, "&search=perl")
			fake_php = get_language_count(city_url, "&search=php")
			fake_python = get_language_count(city_url, "&search=python")
			fake_r  = get_language_count(city_url, "&search=r")
			fake_ruby = get_language_count(city_url, "&search=ruby")
			fake_rust  = get_language_count(city_url, "&search=rust")
			fake_scala = get_language_count(city_url, "&search=scala")
			fake_swift = get_language_count(city_url, "&search=swift")
			fake_typeScript = get_language_count(city_url, "&search=typescript")
			fake_visual_basic = get_language_count(city_url, "&search=visual")
			fake_asp_net = get_language_count(city_url, "&search=asp")
			fake_angular = get_language_count(city_url, "&search=angular")
			fake_bootstrap = get_language_count(city_url, "&search=bootscrap")
			fake_django = get_language_count(city_url, "&search=django")
			fake_ember = get_language_count(city_url, "&search=ember")
			fake_flask = get_language_count(city_url, "&search=flask")
			fake_laravel = get_language_count(city_url, "&search=laravel")
			fake_node_js = get_language_count(city_url, "&search=node")
			fake_rails = get_language_count(city_url, "&search=rails")
			fake_react = get_language_count(city_url, "&search=react")
			fake_spring = get_language_count(city_url, "&search=spring")
			fake_vue_js = get_language_count(city_url, "&search=vue")
			fake_ms_sql = get_language_count(city_url, "&search=mssql")
			fake_mongoDB = get_language_count(city_url, "&search=mongodb")
			fake_my_sql = get_language_count(city_url, "&search=mysql")
			fake_postGreSql = get_language_count(city_url, "&search=postgresql")
			fake_redis = get_language_count(city_url, "&search=redis")
			fake_sqlite = get_language_count(city_url, "&search=sqlite")
		except:
			pass

		lang = Languages.objects.get_or_create(city=city, c=fake_c, c_plus = fake_cplus, c_sharp = fake_csharp,
        dart = fake_dart, go=fake_go, haskell=fake_haskell, html_css= fake_html, java=fake_java, javaScript=fake_javascript,
        kotlin=fake_kotlin, matLab=fake_matLab, obj_c=fake_matLab, perl =fake_perl, php=fake_php ,python =fake_python, r=fake_r,
        ruby=fake_ruby, rust=fake_rust, scala=fake_scala, swift=fake_swift, typeScript=fake_typeScript, visual_basic=fake_visual_basic,
        asp_net = fake_asp_net, angular=fake_angular, bootstrap=fake_bootstrap, django=fake_django, ember=fake_ember, flask=fake_flask,
        laravel = fake_laravel, node_js=fake_node_js, rails=fake_rails, react=fake_react, spring=fake_spring, vue_js=fake_vue_js, ms_sql=fake_ms_sql,
        mongoDB=fake_mongoDB, my_sql=fake_my_sql, postGreSql=fake_postGreSql, redis=fake_redis, sqlite=fake_sqlite)[0]

if __name__ == '__main__':
	print("populating script!")
	populate()
	print('Population complete!')