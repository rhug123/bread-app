import streamlit as st
import numpy as np
import datetime as dt
import time
import pytz
import qrcode
from PIL import Image


st.set_page_config(
    page_title="Fridge Method",
    page_icon="🥶",
)

grams_d = {'flour':126,'salt':16,'yeast':4,'water':240}
cost_d = {'flour':0.001014127233285,'salt':0.002566176470588,'yeast':0.055663716814159,'water':0.000000396258079,'oven':0.005833333333333}

class Bread:

    def __init__(self,flour,salt,yeast,water,oven,salt_pct,yeast_pct,water_pct):
        self.flour = flour
        self.salt = salt
        self.yeast = yeast
        self.water = water
        self.oven = oven
        self.salt_pct = salt_pct
        self.yeast_pct = yeast_pct
        self.water_pct = water_pct

    def g_conv(self,type):
        return grams_d.get(type) * vars(self).get(type)

    def cost(self,type):
        return self.g_conv(type) * cost_d.get(type)

    def total_cost(self):
       return sum([d1.get(k) * getattr(fm,k) * d2.get(k) for d1,d2 in [[{**grams_d,**{'oven':70}},cost_d]] for k in list(d2)])


fm = Bread(3.25,1,1,1.5,1,.039,.009766,.879)






st.sidebar.title('Info')
fm.flour = st.sidebar.number_input('Flour Amount (Cups):',min_value = 0.0,value = fm.flour,step=.25)


flour_grams = fm.flour * 126
fm.salt = (fm.g_conv('flour') * fm.salt_pct) / grams_d.get('salt')
fm.yeast = (fm.g_conv('flour') * fm.yeast_pct) / grams_d.get('yeast')
fm.water = (fm.g_conv('flour') * fm.water_pct) / grams_d.get('water')




st.sidebar.markdown('can feed {:,.0f} people'.format((fm.flour/3.25) * 6))



st.sidebar.markdown('estimated cost ${:,.2f}'.format(fm.total_cost()))



tz = pytz.timezone('EST')
t = dt.datetime.now(tz = tz)
t = t.replace(minute = (t.minute//15) * 15)
year = t.year
month = t.month
day = t.day
hour = t.hour
minute = t.minute
bulk_time = st.sidebar.number_input('Bulk Time (Hours):',min_value = 16,max_value = 72,value = 16,step=1)
final_proof_time = 3
bake1_time = 30
bake2_time = 5
start_date = st.sidebar.date_input('Start Date',dt.date(year,month,day))
start_time = st.sidebar.time_input('Start Time', dt.time(hour,minute))
start_date_time = dt.datetime.combine(start_date,start_time,tzinfo = tz)

d_format = '%x %r'



combine_ingredients = start_date_time
fold1 = (start_date_time + dt.timedelta(minutes=30))
fold2 = (start_date_time + dt.timedelta(hours = bulk_time))
preheat = (start_date_time + dt.timedelta(hours = bulk_time + final_proof_time - .5))
bake1 = (start_date_time + dt.timedelta(hours = bulk_time + final_proof_time))
bake2 = (start_date_time + dt.timedelta(hours = bulk_time + final_proof_time,minutes= bake1_time))
cool = (start_date_time + dt.timedelta(hours = bulk_time + 3,minutes= bake1_time + bake2_time))
bread_finished = (start_date_time + dt.timedelta(hours = bulk_time + final_proof_time,minutes= bake1_time + bake2_time))

total_time = ((bread_finished - combine_ingredients).seconds // 60)
normalized_time = 1 / total_time


estimated_finish = start_date_time + dt.timedelta(hours = bulk_time) + dt.timedelta(hours = 3)
st.sidebar.text('{} Start Time'.format(combine_ingredients.strftime(d_format)))
st.sidebar.text('{} Finish Time'.format(bread_finished.strftime(d_format)))
st.sidebar.subheader('Sparknote Recipe')
st.sidebar.markdown("""1. Mix dry ingredients together
2. Mix in water. Stretch and Fold, and put in fridge 
3. Stretch and fold again after 30 minutes.
4. Place in fridge for {} hours.
5. Shape dough
6. Put on parchment paper with corn meal and let rest for 3 hour final proof
7. Preaheat oven with dutch oven inside to 450°.
8. Once oven is preheated, place in dutch oven with lid on. After 30 minutes, remove lid for final 5 minute bake
9. Remove bread from dutch oven and place on cooling rack. Wait 30 minutes before eating as steam inside is still baking bread.""".format(bulk_time))
st.sidebar.subheader('Schedule')





st.sidebar.markdown("""{} - Combine Ingredients  
{} - Stretch and fold  
{} - Shaping and final proof.  
{} - Preheat oven  
{} - Bake for 35 minutes at 350°  
{} - Bake without lid for 5 minutes  
{} - Cool for 30 minutes  
{} - Bread is ready""".format(combine_ingredients.strftime(d_format),fold1.strftime(d_format),fold2.strftime(d_format),preheat.strftime(d_format),bake1.strftime(d_format),bake2.strftime(d_format),cool.strftime(d_format),bread_finished.strftime(d_format)))


#st.markdown("use cold water instead of warm water. this should slow down the fermentation time and allow more time to develop flavor. also, since yeast is okay in cold environments (and not hot), we do not have to worry about the water being too cold. it also will prioritize the autolyse process in the beginning. We also want to increase the salt amount to increase flavor. The tradeoff to the increase in salt is it acts as an inhibitor to yeast growth. This combined with the addition of cold water which also slows yeast growth means we will double the amount of yeast in the original recipe from .25tsp to .5tsp. The fridge to cooler transition should also help the repeatability of the process, since it is not being exposed to ambient temperature directly, it should produce nearly the same results regardless of external environment.")




st.subheader('Ingredients List')

st.text("""
Flour:              {:,.2f} Cups ({:,.1f} grams)
Salt (Kosher):      {:,.2f} Tablespoons ({:,.1f} grams)
Yeast:              {:,.2f} Teaspoons ({:,.1f} grams)
Warm Water (90°):   {:,.2f} Cups ({:,.1f} grams)""".format(fm.flour,fm.g_conv('flour'),fm.salt,fm.g_conv('salt'),fm.yeast,fm.g_conv('yeast'),fm.water,fm.g_conv('water')))



st.subheader('Recipe Steps')
st.markdown('Mix dry ingredients together in container.')
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/fridge_1.mp4', start_time=0)
st.markdown('After dry ingredients are mixed, add warm water and mix. Once completely mixed, stretch and fold dough. Put lid on container and put into fridge.')
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/fridge_2.mp4', start_time=0)
st.markdown('After 30 minutes, stretch and fold the dough. This helps to mix the dough, as there will be warm spots in the middle after taking out of the fridge. Once done, put back into fridge for {} hours for bulk fermentation.'.format(bulk_time))
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/fridge_3.mp4', start_time=0)


st.markdown("""After {} hours get a piece of parchment paper and put a light amount of corn meal or flour on it.  

Wet your hands with cold water and fold the dough like the video below. Using water will help make sure the dough does not stick to your hands.

Once in a ball, pinch the bottom to form seal. The dough can be further formed into a ball to build more tension.  

Once finished, lift and put dough on parchment paper which has cornmeal or flour sprinkled on it. Lift parchment paper that now has the dough on it back into bowl and cover for another 3 hours.  
You will need to preheat your oven after 2.5 hours to 450° with dutch oven inside.""".format(bulk_time))
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/fridge_4.mp4', start_time=0)
st.markdown("""After 3 hours, score bread (scissors are easiest but not necessarily the best),lift parchment paper into dutch oven, dust top of dough with corn meal, place lid on dutch oven and place into oven at 450°.""")
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/fridge_5.mp4', start_time=0)
st.markdown(" Bake for 30 minutes with lid on, and 5 minutes with the lid off.")
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%207.mp4', start_time=0)
st.markdown("Place on cooling rack for at least 30 minutes. The bread is still cooking on the inside when it's cooling.")


st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/fridge_6.mp4', start_time=0)


minutes_to_fold = (fold1-combine_ingredients).seconds // 60
minutes_to_ferment = (fold2 - fold1).seconds // 60
minutes_till_preheat = (preheat - fold2).seconds // 60
minutes_till_bake1 = (bake1 - preheat).seconds // 60
minutes_till_bake2 = (bake2 - bake1).seconds // 60
minutes_till_cool = (cool - bake2).seconds // 60

headstart = (t - start_date_time) // dt.timedelta(minutes = 1)

progress_texts = [':blue[time till stretch and fold]',':violet[fermentation time]',':blue[preheat oven]',':blue[bake for 35 minutes]',':blue[bake for 5 minutes with lid off]',':blue[let cool]']
progress_times = [minutes_to_fold,minutes_to_ferment,minutes_till_preheat,minutes_till_bake1,minutes_till_bake2,minutes_till_cool]
progress_times_array = np.where((np.array(progress_times).cumsum() - headstart) <= 0,0,np.array(progress_times))



start = headstart * normalized_time
start = max(0,start) if start < 1 else 1
bar = st.sidebar.progress(0,'start')

if st.sidebar.button('Select Time Above and Start'):
    for texts,times in zip(progress_texts,progress_times_array):
        for i in range(times):
            bar.progress(round(start + normalized_time,1),texts)
            time.sleep(60)
            start += normalized_time
    bar.progress(100,'finished')


ical_details = '''
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:Time To Fold Bread
DTSTART;TZID=America/New_York:{}
DURATION:PT1H
LOCATION:Bread
END:VEVENT
END:VCALENDAR
'''.format(fold2.strftime('%Y%m%d') + 'T' + fold2.strftime('%H%M') + '00Z')

img = qrcode.make(ical_details)
st.sidebar.image(Image.fromarray(np.array(img)))

