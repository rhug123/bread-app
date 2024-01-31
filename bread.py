import streamlit as st
import datetime as dt

st.title('No Knead Bread')
st.subheader('Using Cold Water - Minimal Mess')

st.sidebar.title('Info')
flour_cups = st.sidebar.number_input('Flour Amount (Cups):',min_value = 0.0,value = 3.33,step=.3333333)
st.sidebar.markdown('can feed {:,.0f} people'.format((flour_cups/3.33) * 6))

flour_grams = flour_cups * 126
salt_grams = flour_grams * .038095238095238
yeast_grams = flour_grams * 0.004761904761905
water_grams = flour_grams * 0.857142857142857

salt_grams_per_tablespoon = 16
yeast_grams_per_teaspoon = .25
water_grams_per_cup = 240

flour_cost_per_gram = 0.001014127233285
salt_cost_per_gram = 0.002566176470588
yeast_cost_per_gram = 0.055663716814159
water_cost_per_gram = 0.000000396258079
oven_cost_per_minute = 0.005833333333333



estimated_cost = (flour_grams * flour_cost_per_gram) + (salt_grams * salt_cost_per_gram) + (yeast_grams * yeast_cost_per_gram) + (water_grams * water_cost_per_gram) + (oven_cost_per_minute * 70)
st.sidebar.markdown('estimated cost ${:,.2f}'.format(estimated_cost))







cooler_bag = st.sidebar.radio('Are you bulk fermenting in a cooler or cooler bag?',['yes','no'])
#temperature = st.sidebar.number_input('what temperature in degrees F is your environment?',70)
t = dt.datetime.now() - dt.timedelta(hours = 5)
t = t.replace(minute = (t.minute//15) * 15)
year = t.year
month = t.month
day = t.day
hour = t.hour
minute = t.minute
bulk_time = 18 if cooler_bag == 'yes' else 15
start_date = st.sidebar.date_input('Start Date',dt.date(year,month,day))
start_time = st.sidebar.time_input('Start Time', dt.time(hour,minute))
start_date_time = dt.datetime.combine(start_date,start_time)

d_format = '%x %r'
combine_ingredients = start_date_time.strftime(d_format)
fold1 = (start_date_time + dt.timedelta(minutes=30)).strftime(d_format)
fold2 = (start_date_time + dt.timedelta(hours = bulk_time)).strftime(d_format)
preheat = (start_date_time + dt.timedelta(hours = bulk_time + 1.5)).strftime(d_format)
bake1 = (start_date_time + dt.timedelta(hours = bulk_time + 2)).strftime(d_format)
bake2 = (start_date_time + dt.timedelta(hours = bulk_time + 2,minutes=35)).strftime(d_format)
cool = (start_date_time + dt.timedelta(hours = bulk_time + 2,minutes=40)).strftime(d_format)
bread_finished = (start_date_time + dt.timedelta(hours = bulk_time + 3,minutes=10)).strftime(d_format)




estimated_finish = start_date_time + dt.timedelta(hours = bulk_time) + dt.timedelta(hours = 3)
st.sidebar.text('{} Start Time'.format(combine_ingredients))
st.sidebar.text('{} Finish Time'.format(bread_finished))
st.sidebar.subheader('Sparknote Recipe')
st.sidebar.markdown("""1. Mix dry ingredients together
2. Mix in water. 
3. Stretch and fold after 30 minutes.
4. Place in cooler for {} hours.
5. After optional 15 minute cool, coil fold and shape dough.
6. Put on parchment paper with corn meal and let rest for 2 hour final proof
7. Preaheat oven with dutch oven inside to 470 degrees.
8. Once oven is preheated, lower to 450 degrees, and place in dutch oven with lid on. After 35 minutes, remove lid for final 5 minute bake
9. Remove bread from dutch oven and place on cooling rack. Wait 30 minutes before eating as steam inside is still baking bread.""".format(bulk_time))
st.sidebar.subheader('Schedule')





st.sidebar.markdown("""{} - Combine Ingredients  
{} - Stretch and fold  
{} - Coil fold and final proof.  
{} - Preheat oven  
{} - Bake for 35 minutes at 350 degrees  
{} - Bake without lid for 5 minutes  
{} - Cool for 30 minutes  
{} - Bread is ready""".format(combine_ingredients,fold1,fold2,preheat,bake1,bake2,cool,bread_finished))


#st.markdown("use cold water instead of warm water. this should slow down the fermentation time and allow more time to develop flavor. also, since yeast is okay in cold environments (and not hot), we do not have to worry about the water being too cold. it also will prioritize the autolyse process in the beginning. We also want to increase the salt amount to increase flavor. The tradeoff to the increase in salt is it acts as an inhibitor to yeast growth. This combined with the addition of cold water which also slows yeast growth means we will double the amount of yeast in the original recipe from .25tsp to .5tsp. The fridge to cooler transition should also help the repeatability of the process, since it is not being exposed to ambient temperature directly, it should produce nearly the same results regardless of external environment.")




st.subheader('Ingredients List')

st.text("""
Flour:              {:,.2f} Cups ({:,.1f} grams)
Salt (Kosher):      {:,.2f} Tablespoons ({:,.1f} grams)
Yeast:              {:,.2f} Teaspoons ({:,.1f} grams)
Cold Water:         {:,.2f} Cups ({:,.1f} grams)""".format(flour_cups,flour_grams,(salt_grams / salt_grams_per_tablespoon),salt_grams,(yeast_grams * yeast_grams_per_teaspoon),yeast_grams,(water_grams / water_grams_per_cup),water_grams))



st.subheader('Recipe Steps')
st.markdown('Gather Ingredients')
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%201.mp4', start_time=0)
st.markdown('Mix dry ingredients together in a bowl.')
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%202.mp4', start_time=0)
st.markdown('After dry ingredients are mixed, add portion of cold water and mix. Do this until all the water is poured in. Once completely mixed, put plastic wrap over bowl and put in cooler/reusable refrigerator grocery bag. Cold water is used to add more time to the bulk fermentation time, which will add to the flavor of the bread.')
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%203.mp4', start_time=0)
st.markdown('After 30 minutes, stretch and fold a few times around the bowl. This help to form the gluten structure, which will help increase the oven spring.')
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%204.mp4', start_time=0)
st.markdown("""Wait {} hours then place dough in fridge for 15 minutes. This step is just to make the next shaping step easier, but can be skipped.  

Next, get a piece of parchment paper and put a light amount of corn meal or flour on it.  

Wet your hands with cold water and do coil folds while dough is still in the bowl until it is ball shaped. Using water will help make sure the dough does not stick to your hands.  

Once in a ball, tuck the dough underneath itself on all sides to further form a ball shape, and to build tension.  

Once finished, lift and put dough on parchment paper which has cornmeal or flour sprinkled on it. Lift parchment paper that now has the dough on it back into bowl and cover for another 2 hours.  
You will need to preheat your oven after 1.5 hours to 470 degrees with dutch oven inside.""".format(bulk_time))
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%205.mp4', start_time=0)
st.markdown("""After 2 hours, score bread (scissors are easiest but not necessarily the best),lift parchment paper into dutch oven, dust top of dough with corn meal, place lid on dutch oven and place into oven at 450 degrees.""")
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%206.mp4', start_time=0)
st.markdown(" Bake for 35 minutes with lid on, and 5 minutes with the lid off.")
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%207.mp4', start_time=0)
st.markdown("Place on cooling rack for at least 30 minutes. The bread is still cooking on the inside when it's cooling.")
st.video('https://raw.githubusercontent.com/rhug123/bread-app/main/Videos/Bread%20Video%208.mp4', start_time=0)
