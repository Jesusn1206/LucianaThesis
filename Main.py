import streamlit as st



st.set_page_config(page_title="Luciana Izquierdo Thesis", layout="wide", page_icon="🔬", initial_sidebar_state="expanded")

IMAGE_LUCIANA = "media/LUCIANA.png"

IMAGE_FIU = "media/FIU_LOGO.png"
IMAGE_BANNER = "media/COVID_BANNER.png"


# create change font size button
# add images
# sidebar
#Define function to load media
def load_media(column, file_path, caption):
    with column:
        if file_path.endswith(".jpeg") or file_path.endswith(".PNG") or file_path.endswith(".jpg") or file_path.endswith(".png"):
            column.image(file_path, caption=caption,width=300)
        elif file_path.endswith(".mp4"):
            column.video(file_path)
        elif file_path.endswith(".mp3"):
            column.audio(file_path)

def load_media_basic( file_path, caption):

    if file_path.endswith(".jpeg") or file_path.endswith(".PNG")or file_path.endswith(".jpg"):
            st.image(file_path, caption=caption,width=300)
    elif file_path.endswith(".mp4"):
            st.video(file_path)
    elif file_path.endswith(".mp3"):
            st.audio(file_path)


# Define functions to render different pages
def render_home_page():
    st.image(IMAGE_BANNER, use_column_width=True)
    st.title("Myths on Covid Vaccination")
    #st.title("Home")
    st.subheader("Summary")
    st.write("This thesis explores the multifaceted impact of the COVID-19 pandemic on Hispanic culture, encompassing health, socioeconomic, and cultural dimensions. By examining how the pandemic has influenced Hispanic communities, both in terms of direct health outcomes and broader social changes, this research aims to provide a "
             "comprehensive understanding of the unique challenges and responses within these communities.")
    st.divider()






def render_About():
    st.title("About")
    # st.subheader("Get to know the team!")
    st.divider()
    # load_media_basic(IMAGE_JESUS, "Test Caption")
    col1, col2 = st.columns([1,2])
    load_media(col1, IMAGE_LUCIANA, "Luciana Izquierdo Del Barco, MS")

    with col2:
        st.subheader("About")
        st.write("Luciana Izquierdo Del Barco is a Master of Science with a profound interest in studying and researching human behavior and health. With a rich background in communication and science, Izquierdo Del Barco is currently advancing her expertise as a medical student. Her mission is to bridge the gap between"
                 " communication and science, ensuring that complex scientific knowledge is accessible and understandable to the general population.")
        st.write("During their undergraduate studies, Izquierdo Del Barco developed a keen understanding of the intricacies of human behavior through the lens of communication theories and scientific principles. This unique combination of skills has equipped them with the ability to analyze, "
                 "interpret, and effectively communicate scientific data and health information.")
        st.write("As a medical student, Izquierdo Del Barco is dedicated to applying their knowledge to improve public health outcomes. They are particularly interested in how behavioral science can influence health behaviors and promote well-being. By integrating their communication skills with medical expertise,"
                 " Izquierdo Del Barco aims to foster better patient-provider relationships and enhance health literacy among diverse populations.")
        st.write("Izquierdo Del Barco's research interests include the psychological factors influencing health behaviors, the impact of communication strategies on health outcomes, and the development of interventions to address public health challenges. They are committed to conducting research that not only advances"
                 " scientific understanding but also has practical implications for improving health and well-being.")
        st.write("In addition to their academic pursuits, Izquierdo Del Barco actively participates in community outreach programs, leveraging their communication skills to educate the public on various health topics. They believe that empowering individuals with knowledge is key to "
                 "fostering healthier communities.")
        st.write("Through their work, Izquierdo Del Barco strives to be a bridge between the scientific community and the general public, ensuring that scientific advancements translate into meaningful health improvements for all.")


    # load_media(col1, IMAGE_JESUS, "Jesus Elespuru, Senior, Back end, Data-Collection, Florida International University")
    # load_media(col2, IMAGE_ANGIE, "Angie Martinez, Senior, Front end, Data-Collection, Florida International University")
    # load_media(col3, IMAGE_ERNESTO, "Ernesto Rodriguez, Junior, Back end, Florida International University")
    # load_media(col4, IMAGE_MICHEL, "Michel Avalos, Junior, Front end, Florida International University")
    st.divider()

def render_Research():
    st.title("THE INFLUENCE OF MYTHS ON THE HISPANIC COMMUNITY IN THEIR RESISTANCE TOWARDS GETTING THE COVID-19 VACCINATIONS")
    st.subheader("Introduction")
    st.write("Our world was turned upside-down when the news of Covid-19 erupted. With this news, many people felt uncertain about their future. We have been living in quarantine for more than a year, desperate for the world that we knew to return to normal. For centuries humanity has been threatened by many viral diseases, and in 2019, it was the SARS-CoV-2 virus that created despair in our population due to its high mortality rate. The lack of knowledge about this virus and how to combat it was frightening to all. It created global health instability towards our population. "
             "When news of a vaccine emerged to help prevent death against the Coronavirus, many were hoping to return to normalcy. Today, people who are vaccinated are free to roam around the streets without a mask, and they can also be around other people who have also obtained the vaccine.  The vaccine is the epitome of hope for those who believe that this is the way of getting back to normal, yet, there are still many who have their doubts and are abstaining from getting the Covid-19 vaccine.  Thus, limiting the entire population to obtain herd immunity."
             "With a significant number of people having neglected to acquire the vaccine, complications have risen. There are new variants of the Covid -19 virus, such as the Delta variant, that again could lead to fatalities for unvaccinated persons (Nichter, 2020). "
             "In the United States, there are many groups of minorities that are contributing members of our society in which their actions have repercussions on all of us. Thus, when the Center for Disease Control and Prevention (CDC) states that more than half of the population who are white have been vaccinated and that only less than a quarter of Hispanics have been vaccinated—then, this is a worrisome number (American Medical Association COVID-19 VACCINES: PATIENT FAQs, 2021). It makes us question the motives or beliefs as to why the Hispanic population is not getting vaccinated.")

    st.divider()
    st.subheader("Opportunity Statement")
    st.write("Covid-19 has shaken up the world since it arrived, and it has not discriminated infecting any race nor ethnicity. In fact, research has shown that even though minority groups have severe Covid-19 symptoms, they’re the least to get vaccinated; thus, an opportunity is presented to create a campaign targeting specific minority groups, "
             "My specific target audience is Hispanics born in Latin American, who have been embedded different beliefs at a very young age without any scientific knowledge. Acknowledging their behaviors and their culture towards science can help create a campaign that will result in a conduct transformation; in this case the opportunity is for my audience to obtain the Covid-19 vaccine. "
             "An opportunity is presented to originate a behavior change in my target population, and for then to acquire the Covid-19 vaccines. By knowing their motives and beliefs as to why they are not getting vaccinated, I can target a campaign to inform my population and dimmish any gaps in scientific knowledge or uncertainties that Hispanics may have accumulated over the years.")

    st.subheader("Situation Analysis")
    st.subheader("Organization Analysis")
    st.divider()
    st.subheader("History:")
    st.write("Covid-19 emerged at the beginning of December 2019 near Wuhan City, Hubei Province, China. It was the World Health Organization (WHO) who created the name for the disease: coronavirus disease 2019, abbreviated COVID-19. ‘CO’ stands for ‘corona,’ ‘VI’ for ‘virus,’ and ‘D’ for disease. The virus that causes COVID-19, SARS-CoV-2, is a coronavirus. The word corona means crown and refers to the appearance that coronaviruses get from the spike proteins sticking out of them (CDC,2020)."
             "Covid-19 can propagate when an infected person breathes out droplets and small particles that contain the virus. These droplets and particles can be breathed in by other people or land on their eyes, noses, or mouth. In other circumstances, they may contaminate surfaces they touch. People who are closer than 6 feet from the infected person are most likely to get infected, thus the CDC enforced rules to limit propagation. "
             "There are many ways one can protect themselves to not get infected; by wearing a mask that covers your nose and mouth to help protect yourself and others. Also, by staying at least six feet away from another person, but the proven statistic that lowers chances of contracting the virus is by getting vaccinated as soon as possible. "
             "When a vaccinated individual is exposed to the disease, the body can more readily and quickly respond and neutralize the disease. The vaccine helps the body’s immune system battle and respond to severe disease such as the Covid-19. Given the benefits of vaccines, global efforts for a vaccine for COVID-19 have been massive (CDC). "
             "Vaccines could not only protect individuals, but if large enough populations received them, a COVID-19 vaccine could protect those who were ineligible to receive a vaccine through herd immunity (Nichter, 2020)."
             "While wearing a mask cuts your own risk by 65 percent(Your Mask Cuts Own Risk by 65 Percent, 2020), the Covid-19 vaccine has proven to be the most effective. For example, it was noted that even though the efficacy of Pfizer’s coronavirus vaccine steadily declines to about 84% about six months after a second dose, according to CEO Albert Bourla. The latter option would be best to procure one’s health (Stankiewicz, 2021). While there will always be a risk of contracting the virus, it is statistically proven that less severe symptoms would occur to those who have gotten vaccinated. "
             "The Covid-19 vaccine, which is made of mRNA, a genetic material, teaches a person’s cells how to make copies of the spike proteins. So, that if later a person is exposed to the virus, the body will recognize it and would know how to fight it off (How MRNA COVID-19 Vaccines Work, n.d.) this has proven to be the better option to combat the Covid-19. "
             "While options and different locations have been scattered across South Florida for people to get vaccinated—this still is an uphill battle. By the end of Summer 2021, hospitals reported that over 90% of Covid-19 patients had not gotten immunized (Selig, 2021). "
             "Information and access to the vaccine is given to the public, yet, South Florida’s populations is seemingly reluctant to getting the vaccine. When one digs further to the cause, one notes that while most of the South Florida population are Hispanics, most of them have cultural and religious beliefs on why getting vaccinated is a potential risk. "
             "On April 2021, the Miami Herald report that many Hispanics are reporting to have many challenges to obtain the vaccine. “Some of the limitations, which affect all Hispanics regardless of their race and socioeconomic status, include the inability to miss a workday to get vaccinated, lack of legal documentation, not being able to speak English or Spanish (some only speak indigenous languages from Latin America), mistrust in the healthcare industry and misinformation about the COVID-19 vaccine.” (Miami Herald, 2021) "
             "While many efforts have been disseminated across the country to get people to get vaccinate, it seems as if this matter is still an uphill battle. Recently the White House declared a $10 billion investment to expand access to covid-19 vaccines and build vaccine confidence in high-risk communities. Thus, trying to procure the safety of all its population, and with the mission of educating the American rural population on the importance of getting vaccinated. To benefit populations with increased prevalence of Covid-19 and disproportionately impacted by long-standing health disparities the White House aims to reduce the gap of misconceptions that leads to vaccine hesitancy that looms in many. "
             "Vaccines The practice of immunization dates back hundreds of years. In the 17th century Buddhist monks drank snake venom to confer immunity of snake bite, this has been date as the first glimpse of immunization against adverse pathogens. Physician Edward Jenner is recognized as the father of immunology worldwide.  He presented the concept of inoculation back in 1796, Jenner inoculated an eight-year-old boy by taking pus from the cowpox lesions on a milkmaid’s hands and introducing the fluid into a cut he made in the boy’s arm. Six weeks later, Jenner exposed the boy to smallpox, but he did not develop the infection then, or on 20 subsequent exposures. Thus, he had created the first ever vaccine "
             "against smallpox (A Brief History of Vaccines and How They Changed the World, 2020). Today, it’s rutinary for a child to obtain the small pock’s vaccine, yet back in the 18th century this news caused a frenzy, that even though the undeniable response to the vaccine was document many were scare leading many countries to enforce mandatory small pock vaccinations. "
             "While fear of the unknown foreshadows the Coronavirus pandemic and any viral outbreaks that have been recurrent through the years, it it’s important to note that the power of information can truly dimmish vagueness of the subject. Global pandemics are not something new, ever since humans learned to live in groups forming communities where they live close to each other and travel across the seas, the world has seen numerous diseases spread like wildfire. "
             "Whether it was one of the first pandemics recorded, like the Antonine Plague (165 AD-180 AD), or the recent Covid-19 pandemic (Plotkin, 2014), one thing that it’s undeniable is the vast number of lives that have been marginalized and taken from this world because of  the lack of knowledge in combating  the virus. ")
    st.divider()
    st.subheader("Background:")

    st.write("Vaccinating a high percentage of the population against Covid-19 is a major part of the U.S. strategy to reduce the pandemic with the initiative of creating herd immunity. Since the Covid-19 vaccine distribution began in the United States on Dec. 14, more than 304 million doses have been administered, fully vaccinating over 141 million people or 42.5% of the total U.S. population (NPR,2021). "
             "After a measured start in December, vaccine management progressed in scale and efficiency. The U.S. exceeded President Joe Biden's primary wishes of having one hundred million vaccines by the first one hundred days, accomplishing 2 hundred million vaccines by the 92nd day. Inoculations rates peaked in early April — with the United States administering more than three million Covid-19 vaccines per day."
             " Today vaccine eligibility is open to anyone as young as 12-years old to get vaccinated. Unfortunately, the number of people getting vaccinated has declined, as soon as individuals who had been keen to get vaccinated obtained their shots (NPR,2021). Different initiatives nationwide have been aimed at people to take charge and get vaccinated. Yet, this has seemed to fail in creating a call to action towards the population. "
             "Different media outlets have plagued their platforms with Covid-19 vaccine information that have seemed to pass inadvertently by their population, hence the low vaccination turnout has still not decreased. Sadly, states are progressing unevenly in their vaccine rollout. Florida is 28th on the list of the 51 states, with less than half the population being vaccinated."
             " The Ad Council and the COVID Collaborative have unveiled a brand new public marketing campaign geared toward creating trust amongst Americans who are hesitant about getting the COVID-19 vaccine (Harvard, 2020), The “It’s Up To You” marketing campaign will be in English and Spanish for TV, billboards, social media posts. It will try to be tailored to the Black and Hispanic communities, "
             "in which COVID-19 has hit tough however wherein vaccine uptake has lagged. Some of the advertisements may also function celebrities, such as; Angela Bassett, Sanjay Gupta, and Anthony Fauci, the nation’s pinnacle infectious illnesses expert (ABC News,2020). Not too long-ago, numerous campaigns about Covid-19 vaccination have been emerging. Such as Walgreens teaming up with John Legend for the ""This Is Our Shot"" campaign "
             "encouraging Americans to get vaccinated against COVID-19. Planned Parenthood used $2 million on a bilingual ad campaign encouraging COVID-19 vaccinations. In Florida, Florida's Orange County launched its “I Got My Shot” campaign to encourage COVID-19 vaccinations, with promotional support from Walt Disney World and Universal Orlando, and in South Florida, the Health Foundation of South Florida teamed up with Miami-Dade County "
             "and Broward County to launch its ""I Did It"" campaign, which encourages people to get vaccinated against COVID-19 (Madison, Shrout, Renna, & Kiecolt-Glaser, 2021). Different initiatives have been pouring to incentivize the population to obtain their Covid-19 vaccine, and to this day none have been effective in targeting the motives as to why many people are not getting vaccinated.")
    st.divider()
    st.subheader("Consumer Analysis")
    st.subheader("Hispanics:")

    st.write("	My target audience are born and raised Latin American Hispanics that have immigrated to South Florida. Their age can range from 40 to 60-year-olds. My target audience is people who have their core values and traditions from different parts of Latin America. "
             "Many have been accustomed to their traditions and their religion that they may be aloof to different scientific facts about the Covid-19 vaccine. Hence my population is adults that are already set on their cultural core values towards every subject in life, it can be difficult to make them change their perspective. Learning about their different cultures and their worries about getting the Covid-19 vaccine "
             "can help target the campaign. By ethnicity, 26.1% of the population is Hispanic-Latino (of any race) and 73.9% is non-Hispanic (of any race). If dealt with as a separate category, Hispanics are the biggest minority in Florida (Madison, Shrout, Renna, & Kiecolt-Glaser, 2021). To achieve a maximum outcome in the campaign that can be measured by the number of Hispanics that get vaccinated, one must specifically target "
             "the limitations this population presents. It is alarming the rate of Hispanics that are not getting vaccinated, even when they have been one of the groups that have severely endured the repercussion of the Coronavirus. The CDC reported that the share of vaccinations received by Hispanic people is similar to or higher than their share of deaths in most reporting states, although in some states it continues to be lower. "
             "For example, in Colorado, 11% of vaccinations have gone to Hispanic people, while they account for 42% of cases, 25% of deaths, and 22% of the total population in the state (CDC, 2021). ")

    st.divider()
    st.subheader("Market Analysis")

    st.write("The CDC states, “The federal government is providing the vaccine free of charge to all people living in the United States, regardless of their immigration or health insurance status.” While the vaccine has been said to be free, many marketing strategies lack to also clarify their side-effects (Carlsen, Huang, Levitt, & Wood, 2021). "
             "Almost every day there’s a new case of Covid-19, one that could have been stopped if people would get immunized. But, because some might believe the marketing strategy is obscure or difficult to comprehend –then, they must be hiding some facts. "
             "The reality is that the vaccines have passed through trial-and-error phases in the labs and that before inoculating the population with the vaccine – procedures to limit risk were considered. The Covid-19 vaccine marketing strategy lacks clarity, it doesn’t stipulate nor target the specific Hispanics who are worried about receiving the vaccine."
             " Hispanics can have different cultural beliefs that make them not want to get the vaccine, but if there was a marketing strategy to bridge the gap of misinformation and teach them about clinical procedures—then, most would get vaccinated. Most actions are caused by a reaction, if one acknowledges and gives out clear information to individuals, then "
             "they will comprehend and respond with the proper action. In this case, that call to action would be to get vaccinated and learn about the risks of contracting Covid-19. "
             "After being fully vaccinated, one can enjoy their life back to the new normal. While getting this vaccine, it usually can take around 2 weeks for our body to create immunity against the virus –thus, it is recommended to stay inside and wear protective gear until the two weeks are up.")

    st.divider()
    st.subheader("Competative Analysis")

    st.write("While different Covid-19 campaigns try to battle it out for the attention of the Hispanic population, one important factor to note is the amount of misinformation that they are being plagued with. While one would tell them, it’s very easy to get the vaccine and that it is pain-free, another Ad would list all the recommendations and side-effect of getting that same vaccine. "
             "This leads people to wonder, why are they hiding some of the scientific facts –but ultimately it leads people to lose trust and focus on why it is important to get the Covid-19 vaccine. "
             "So much misinformation and so many different facts are given to the population daily. Instead of explaining the risks and as to why one can get a blood clot, the media frames the information and groups people into the same category to receive more clicks and views on their webpage.  When, the only thing they are growing is fear from the already uncertain group of people who don’t know if they should get vaccinated."
             " As the world progresses many media outlets have grown exponentially, they have formed conglomerates and it can be hard to trust big companies' motives when they are interfering with one's health. But, instead, if one were to lead a simple and concise campaign targeting the worries of our population, a different outcome could be achieved."
             " Our population is people with different bits of knowledge, a different cultural background and they must be aware that while the vaccine is new and is man-made, that no potential risk of harming one's culture would it inflict, Campaigns need to touch about the culture, religion, the unclear messaging, and the obvious anti-vaxxers who are spreading a false narrative.")

    st.subheader("Vaccine Brands")

    st.write("There are 3 vaccines in the United States, In August 2021, Pfizer-BioNTech became the first Covid-19 vaccine to receive full approval for people ages 16 and older from the Food and Drug Administration (FDA) for use in the U.S. In December, it was the first COVID-19 vaccine to receive FDA Emergency Use Authorization (EUA), after the company reported positive initial clinical trial data"
             " that showed the vaccine was highly effective at preventing symptomatic disease. This is a messenger RNA (mRNA) vaccine, which uses a relatively new technology. It must be stored in freezer-level temperatures, which can make it more difficult to distribute than some other vaccines (Katella, 2021). "
             "The FDA placed a warning label on the Pfizer vaccine regarding a “likely association” with reported cases of heart inflammation in young adults. This inflammation may occur in the heart muscle and is considered important but uncommon arising in about 12.6 cases per million second doses administered. The inflammation, "
             "in most cases, gets better on its own without medical intervention (Katella, 2021). Pfizer’s initial Phase 3 clinical data presented in December showed its vaccine to have 95% efficacy. Yet a new Mayo Clinic preprint looked at the effectiveness of mRNA vaccines between January and July. It found Pfizer effectiveness dropped to "
             "42% in Minnesota in July, when Delta became the dominant strain. "
             "Moderna’s vaccine was authorized for emergency use in the U.S. last December, about a week after the Pfizer vaccine. Moderna uses the same mRNA technology as Pfizer and has a similarly high efficacy at preventing symptomatic disease. It also needs to be stored in freezer-level temperatures. "
             "In mid-August, the FDA approved a booster dose of the Moderna vaccine for certain immuno-compromised individuals, including solid organ transplant recipients and those with conditions that give them an equally reduced ability to fight infections and other diseases. In one CDC study, data from the state "
             "of New York showed vaccine effectiveness dropping from 91.7 to 79.8% against infection. For adults 18 and older, they can also use the Johnson & Johnson’s vaccine "
             "which the FDA granted permission in February 2021. Unlike the Pfizer and Moderna vaccines, this is a carrier, or virus vector, vaccine. It can be stored in normal refrigerator temperatures, and because it requires only a single shot, it is easier to distribute and administer. In a recent study the Johnson & Johnson’s had a promising "
             "outcome in protecting against the delta variant. The delta variant, which first appeared in December 2020, is a highly transmissible version of the coronavirus "
             "that is said to spread as easily as chickenpox. In June, 30% of the new COVID-19 cases were the delta variant. “Current data for the eight months studied so far show that the single-shot Johnson & Johnson COVID-19 vaccine generates a strong neutralizing antibody response"
             " that does not wane,” said Mathai Mammen, the global head of Janssen Research & Development at Johnson & Johnson, in a press release (Johnson & Johnson, 2021).")


    st.divider()
    st.subheader("References")
    st.write("A brief history of vaccines and how they changed the world. (2020, April 9). World Economic Forum. https://www.weforum.org/agenda/2020/04/how-vaccines-changed-the-world/")
    st.write("American Medical Association COVID-19 VACCINES: PATIENT FAQs. (2021, March 16). AMA. https://www.ama-assn.org/system/files/2020-12/covid-19-vaccine-patient-faqs.pdf")
    st.write("Carlsen, A., Huang, P., Levitt, Z., & Wood, D. (2021, June 08). How Is The COVID-19 Vaccination Campaign Going In Your State? Retrieved from https://www.npr.org/sections/health-shots/2021/01/28/960901166/how-is-the-covid-19-vaccination-campaign-going-in-your-state")
    st.write("Florida's Black, Hispanic communities lag behind in COVID-19 vaccination rates, data shows. (2021, April 29). Retrieved from https://www.local10.com/news/local/2021/04/29/floridas-black-hispanic-communities-lag-behind-in-covid-19-vaccination-rates-data-shows/")
    st.write("House, T. W. (2021, March 25). FACT SHEET: Biden Administration Announces Historic $10 Billion Investment to Expand Access to COVID-19 Vaccines and Build Vaccine Confidence in Hardest-Hit and Highest-Risk Communities. The White House. https://www.whitehouse.gov/briefing-room/statements-releases/2021/03/25/fact-sheet-biden-administration-announces-historic-10-billion-investment-to-expand-access-to-covid-19-vaccines-and-build-vaccine-confidence-in-hardest-hit-and-highest-risk-communities/")
    st.write("How mRNA COVID-19 Vaccines Work. (n.d.). CDC. Retrieved July 10, 2021, from https://www.cdc.gov/coronavirus/2019-ncov/downloads/vaccines/COVID-19-mRNA-infographic_G_508.pdf")
    st.write("Inequities In Florida’s Vaccine Distribution Persist For Some. (2021, September 17). WUSF Public Media. https://wusfnews.wusf.usf.edu/health-news-florida/2021-09-15/inequities-in-floridas-vaccine-distribution-persist-for-some")
    st.write("Johnson & Johnson. (2021, July 1). Content Lab U.S. https://www.jnj.com/positive-new-data-for-johnson-johnson-single-shot-covid-19-vaccine-on-activity-against-delta-variant-and-long-lasting-durability-of-response")
    st.write("Katella, K. (2021, September 17). Comparing the COVID-19 Vaccines: How Are They Different? Yale Medicine. https://www.yalemedicine.org/news/covid-19-vaccine-comparison")
    st.write("Madison, A. A., Shrout, M. R., Renna, M. E., & Kiecolt-Glaser, J. K. (2021). Psychological and Behavioral Predictors of Vaccine Efficacy: Considerations for COVID-19. Perspectives on Psychological Science, 16(2), 191-203. doi:10.1177/1745691621989243")
    st.write("Miami Herald. (2021). The Miami Herald. https://account.miamiherald.com/paywall/subscriber-only?resume=250594469&intcid=ab_archive")
    st.write("Nambi Ndugga Follow @nambinjn on Twitter, O. (2021, June 07). Latest Data on COVID-19 Vaccinations Race/Ethnicity. Retrieved from https://www.kff.org/coronavirus-covid-19/issue-brief/latest-data-on-covid-19-vaccinations-race-ethnicity/")
    st.write("Nichter, M. (2020, December 16). COVID-19 Vaccines An overview of COVID-19 vaccines, their distribution, and acceptance and hesitation. HCW HOSTED. https://medanthcovid19.files.wordpress.com/2021/01/covid-19-primer-vaccines-12-18.pdf")
    st.write("Plotkin, S. (2014, August 18). History of vaccination. US National Library of Medicine National Institutes of Health. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4151719/")
    st.write("Selig, D. (2021, July 21). How many COVID-19 patients in South Florida were vaccinated? WPLG. https://www.local10.com/news/local/2021/07/21/how-many-covid-19-patients-in-south-florida-were-vaccinated/")
    st.write("Stankiewicz, K. (2021, July 28). Pfizer’s CEO says Covid vaccine effectiveness drops to 84% after six months. CNBC. https://www.cnbc.com/2021/07/28/pfizers-ceo-says-covid-vaccine-effectiveness-drops-to-84percent-after-six-months.html")
    st.write("Your Mask Cuts Own Risk by 65 Percent. (2020, October 28). UC Davis. https://www.ucdavis.edu/coronavirus/news/your-mask-cuts-own-risk-65-percent")




with st.sidebar:
    st.image(IMAGE_FIU,width=100)
    st.title("Learn More")
    page = st.sidebar.selectbox("Page", options=["Home", "Research", "About"])


# Conditionally render pages based on selection
if page == "Home":
    render_home_page()
elif page == "About":
    render_About()
elif page == "Research":
    render_Research()