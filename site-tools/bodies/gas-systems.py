SLUG = 'gas-systems'
SERVICE_NAME = 'Gas Systems'
KEYWORD = 'gas line'
SECONDARY_KEYWORDS = ['propane', 'natural gas', 'gas appliance', 'gas leak']
TITLE = 'Gas Line Services in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Gas line installation, repair and appliance hookups in New Milford, Danbury and nearby CT towns. '
               'Propane and natural gas, licensed master plumber.')
IMAGE = None

HERO = dict(
    eyebrow='Gas systems · New Milford, CT',
    h1='Gas line installation &amp; repair in New Milford, CT',
    lead=('Adding a gas range, a generator, a fireplace or a tankless water heater? Get new gas lines and '
          'appliance connections installed safely, to code, by a licensed master plumber.'),
    cta='Get a free gas line quote',
    panel=dict(title='Common gas line projects', items=[
        'Gas ranges and cooktops',
        'Dryers and gas appliances',
        'Tankless and gas water heaters',
        'Fireplaces and outdoor grills',
        'Standby generators',
        'Gas line repairs and upgrades'],
        call_text='Smell gas? Leave first, then call your gas supplier or 911.'),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What gas line installation involves',
         intro=('Gas work has no margin for error. A proper gas line installation is sized for every appliance it '
                'serves, built with approved materials and tested for leaks before anything is lit.'),
         paras=['Whether you use natural gas or propane, gas line work typically includes:'],
         blocks=[dict(type='checklist', items=[
             'Calculating demand for every gas appliance',
             'Sizing pipe for the length of the run and the load',
             'Running new gas piping to the appliance location',
             'Shut-off valves at each appliance',
             'Appliance connections and sediment traps',
             'Pressure-testing the new piping for leaks',
             'Checking appliance operation after connection',
             'Permits and inspection where required'])]),
    dict(id='warning-signs', eyebrow='When to call', h2='Signs you need gas line work',
         intro='Most gas line projects come from one of these situations:',
         blocks=[dict(type='cards', cols=3, items=[
             ('Adding a gas appliance', 'A new range, dryer, fireplace or grill needs its own properly sized line and shut-off valve.'),
             ('Switching to tankless', 'Tankless water heaters often need a larger gas line than the old tank did.'),
             ('Installing a generator', 'Standby generators need a dedicated gas supply sized for their load.'),
             ('Remodeling a kitchen', 'Moving or adding a range means moving or extending the gas line before walls and cabinets go in.'),
             ('Old or corroded piping', 'Rusted or outdated gas piping should be inspected and replaced before it becomes a problem.'),
             ('Appliances underperforming', 'Weak flames or appliances that won&rsquo;t stay lit can point to undersized or restricted gas lines.')])],
         callout=('<strong>Smell gas?</strong> Don&rsquo;t use switches, phones or flames inside. Leave the building '
                  'right away and call your gas supplier or 911 from outside. Once it&rsquo;s safe, we can repair '
                  'the line.')),
    dict(id='options', eyebrow='Project options', h2='Gas line installation options',
         intro='The most common gas line projects we help homeowners and builders with:',
         blocks=[dict(type='options', items=[
             ('Most common', 'Appliance gas connections', 'New lines and connections for ranges, cooktops, dryers and other gas appliances.', ['Properly sized supply', 'Dedicated shut-off valve', 'Leak-tested connection']),
             ('Upgrades', 'Tankless &amp; generator lines', 'Larger supply lines for high-demand equipment like tankless water heaters and standby generators.', ['Sized for the full load', 'Coordinated with installers', 'Code-compliant work']),
             ('Outdoor living', 'Grills, fire pits &amp; heaters', 'Permanent gas lines for outdoor kitchens, grills and fire features, so you never swap a tank again.', ['Fixed gas supply', 'Outdoor shut-off', 'Clean, safe routing']),
             ('Repairs', 'Gas line repair &amp; replacement', 'Repair or replacement of damaged, leaking or outdated gas piping.', ['Leak testing', 'Updated materials', 'Peace of mind'])])]),
    dict(id='considerations', eyebrow='Project considerations', h2='What to consider before adding a gas line',
         intro='These details decide how the gas line is designed and what it costs.',
         blocks=[dict(type='consider', items=[
             ('Natural gas or propane', 'Many homes in our area use propane from a tank rather than utility gas. Appliances and piping are set up for the fuel you have.'),
             ('Total demand', 'Every gas appliance adds to the load. A line that worked for a stove may be too small once a tankless heater is added.'),
             ('Distance &amp; routing', 'The length of the run and how the pipe gets there affect pipe size, labor and cost.'),
             ('Supply capacity', 'Your meter, regulator or propane setup must be able to supply the new load. Your gas supplier may need to be involved.'),
             ('Permits &amp; inspection', 'New gas piping requires a permit and inspection in Connecticut towns.'),
             ('Ventilation', 'Gas appliances need proper venting and combustion air. Planning for it up front avoids problems later.')])]),
    dict(id='process', eyebrow='How it works', h2='Our gas line installation process',
         intro='Safety first at every step, with a clear price before work begins.',
         blocks=[dict(type='steps', items=[
             ('Request a visit', 'Call us or send the form below with the appliance or project you have in mind.'),
             ('On-site assessment', 'We look at your gas supply, the route and every appliance on the system.'),
             ('Clear, written quote', 'You get a written quote before anything starts. No obligation and no surprises.'),
             ('Installation', 'We run and connect the new gas piping and install shut-off valves.'),
             ('Test &amp; inspect', 'The system is pressure-tested, appliances are checked and inspection is arranged.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why homeowners trust us with their gas line',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Gas line services in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we install and repair gas lines for homeowners and builders across Western '
             'Connecticut, from Brookfield, Danbury and Newtown to Ridgefield, Southbury and Westport. Whether your '
             'home runs on natural gas or propane, we know the setups common in your area.')

ESTIMATE = dict(
    heading='Get your gas line quote',
    lead=('Tell us what you&rsquo;re connecting and where. We&rsquo;ll look at your gas supply and the route and '
          'give you a clear price.'),
    options=[('Gas Line - Appliance', 'New gas line / appliance hookup'), ('Gas Line - Tankless / Generator', 'Tankless water heater or generator'),
             ('Gas Line - Outdoor', 'Grill, fire pit or outdoor line'), ('Gas Line Repair', 'Gas line repair or replacement'),
             ('Other', 'Something else')],
    details_label='Tell us about your gas line project',
    placeholder='e.g. &quot;Switching to a gas range in our kitchen. We have propane and the tank is outside the garage.&quot;',
)
REVIEW = dict(quote=('Cliff was very professional, clear, on time, and the work well done. Arrived when he said he would, '
                     'got right to the job and cleaned up when done. The best recommendation is a job well done'),
              name='Sam G.', initials='SG', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Gas line FAQ'
FAQ_HEADING = 'Gas line questions, answered.'
FAQS = [
    ('How much does it cost to run a new gas line?',
     'It depends on the length of the run, the pipe size needed for your appliances, how the line gets from the '
     'supply to the appliance, and permit requirements. A short connection near the existing line costs far less than '
     'a long run to a generator or outdoor kitchen. We give you a written quote after a free on-site visit.'),
    ('How long does a gas line installation take?',
     'A straightforward appliance connection is often done in a single visit. Longer runs, larger lines or projects '
     'that need a gas supplier or inspection take more time. We will give you a realistic timeline with your quote.'),
    ('Do you work with both propane and natural gas?',
     'Yes. Many homes in our area use propane, while others are on utility natural gas. We set up the piping and '
     'connections for the fuel your home uses.'),
    ('Is a permit required for gas line work in Connecticut?',
     'New gas piping generally requires a permit and inspection from your town. We will explain what your project '
     'needs during the on-site visit.'),
    ('What should I do if I smell gas or suspect a gas leak?',
     'Leave the building right away without using switches, phones or flames inside, and call your gas supplier or '
     '911 from outside. Once the area is safe, call us at <a href="tel:+18602481218">1 (860) 248-1218</a> to repair the problem.'),
]

RELATED_HEADING = 'Other services that go with gas line work.'
RELATED = [
    ('water-heater-installation', 'Gas, tankless and propane water heaters installed with the right supply line.'),
    ('bathroom-remodels', 'Complete remodels and remodel plumbing, coordinated with your other trades.'),
    ('plumbing-repairs', 'Leaks, valves and fixtures throughout the house diagnosed and repaired.'),
]

CTA = dict(h2='Adding a gas appliance?',
           p='Get a free on-site visit and a clear, written quote for your new gas line. No obligation.')
