SLUG = 'water-filtration-treatment'
SERVICE_NAME = 'Water Filtration & Treatment'
KEYWORD = 'water filtration'
SECONDARY_KEYWORDS = ['water softener', 'well water', 'hard water', 'iron filter']
TITLE = 'Water Filtration in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Water filtration, softeners and treatment systems in New Milford, Danbury and nearby CT towns. '
               'Well and city water, licensed master plumber.')
IMAGE = None

HERO = dict(
    eyebrow='Water treatment · New Milford, CT',
    h1='Water filtration &amp; treatment in New Milford, CT',
    lead=('Hard water, rusty stains, odd smells or worries about your well? Get a water filtration or softening '
          'system matched to your water test results, installed by a licensed master plumber.'),
    cta='Get a free water treatment quote',
    panel=dict(title='Common water problems we treat', items=[
        'Hard water scale and spotting',
        'Iron and rust-colored stains',
        'Sediment from private wells',
        'Low pH water and blue-green stains',
        'Chlorine taste and odor on city water',
        'Drinking water filtration']),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What water filtration and treatment involves',
         intro=('The right water filtration system starts with knowing what is actually in your water. Many homes in '
                'our area are on private wells, and well water can change from one street to the next.'),
         paras=['A typical water treatment installation includes:'],
         blocks=[dict(type='checklist', items=[
             'Reviewing your water test results and concerns',
             'Recommending the right equipment for your water',
             'Installing filters, softeners or treatment units',
             'Bypass valves so you can service the system easily',
             'Drain and electrical connections where needed',
             'Setting up and programming the system',
             'Checking pressure and flow after installation',
             'Explaining filter changes and maintenance'])]),
    dict(id='warning-signs', eyebrow='Common problems', h2='Signs you need water treatment',
         intro='Your water usually tells you when something is off. These are the signs we hear about most often:',
         blocks=[dict(type='cards', cols=3, items=[
             ('White scale and spots', 'Crusty buildup on faucets and glassware means hard water, which also shortens the life of water heaters.'),
             ('Orange or brown stains', 'Rust-colored stains in sinks, tubs and toilets point to iron, common in Connecticut well water.'),
             ('Blue-green stains', 'Stains around drains can mean acidic, low-pH water that slowly eats away at copper pipes.'),
             ('Sediment or cloudy water', 'Grit in aerators and cloudy water often come from the well and wear out fixtures.'),
             ('Bad taste or odor', 'A chlorine taste on city water or a sulfur smell on well water are both treatable.'),
             ('Dry skin and dull laundry', 'Hard water makes soap less effective and leaves residue on skin, hair and clothes.')]),
         ],
         callout=('<strong>Test first.</strong> For well water, a test from a state-certified lab tells you exactly '
                  'what you are dealing with, including things you can&rsquo;t see or taste. We will help you choose '
                  'equipment based on those results.')),
    dict(id='options', eyebrow='Treatment options', h2='Choosing the right water filtration system',
         intro='Most homes need one or two of these, sized to your household and your water test:',
         blocks=[dict(type='options', items=[
             ('Hard water', 'Water softeners', 'Removes the minerals that cause scale, protecting your water heater, fixtures and appliances.', ['Less scale and spotting', 'Longer appliance life', 'Softer feel for skin and laundry']),
             ('Whole house', 'Sediment &amp; whole-house filters', 'Catches grit and particles before they reach your pipes, fixtures and appliances.', ['Protects the whole plumbing system', 'Simple cartridge changes', 'Ideal for private wells']),
             ('Well water', 'Iron &amp; pH treatment', 'Iron filters and neutralizers for iron, manganese and acidic water, which are common in local wells.', ['Stops rust and blue-green stains', 'Protects copper piping', 'Matched to your test results']),
             ('Drinking water', 'Under-sink filtration', 'Point-of-use filters, including reverse osmosis, for cleaner-tasting drinking and cooking water.', ['Dedicated drinking faucet', 'Compact under-sink install', 'Easy filter changes'])])]),
    dict(id='considerations', eyebrow='Project considerations', h2='What to consider before installing water treatment',
         intro='A few details decide which system makes sense and how well it works.',
         blocks=[dict(type='consider', items=[
             ('Your water source', 'Private wells and city water have different problems. Well owners are responsible for their own water quality and testing.'),
             ('Test results', 'Treating the wrong problem wastes money. Hardness, iron, pH and other results determine the right equipment.'),
             ('Household size', 'Systems are sized to how much water your home uses. Undersized equipment loses pressure and wears out sooner.'),
             ('Space &amp; connections', 'Most systems install near where water enters the home and may need a drain and an outlet nearby.'),
             ('Maintenance', 'Filters need changing and softeners need salt. Choose a system you are comfortable maintaining.'),
             ('Protecting your home', 'Treating hard or acidic water protects your water heater, pipes and new fixtures from early failure.')])]),
    dict(id='process', eyebrow='How it works', h2='Our water treatment installation process',
         intro='Clear recommendations, a written price and a system you understand.',
         blocks=[dict(type='steps', items=[
             ('Request a visit', 'Call us or send the form below and tell us what you are noticing in your water.'),
             ('Review &amp; assessment', 'We look at your plumbing, your water source and any test results, and talk through options.'),
             ('Clear, written quote', 'You get a written quote for the recommended system before anything starts.'),
             ('Installation', 'We install the equipment with a bypass, make the connections and set up the system.'),
             ('Walkthrough', 'We explain how your system works and what maintenance it needs.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why homeowners choose us for water filtration',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Water filtration in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we install water filtration and softening systems for homeowners across Western '
             'Connecticut, from Brookfield, Danbury and Newtown to Ridgefield, Southbury and Westport. Many homes '
             'here rely on private wells, and we know the hard water, iron and acidity problems they bring.')

ESTIMATE = dict(
    heading='Get your water treatment quote',
    lead=('Tell us about your water: city or well, what you are noticing and any test results you have. '
          'We&rsquo;ll recommend the right system and give you a clear price.'),
    options=[('Water Treatment', 'Not sure, need advice'), ('Water Softener', 'Water softener'),
             ('Whole-House Filtration', 'Whole-house or sediment filter'), ('Iron / pH Treatment', 'Iron or pH treatment'),
             ('Drinking Water Filter', 'Drinking water (under-sink) filter'), ('Other', 'Something else')],
    details_label='Tell us about your water',
    placeholder='e.g. &quot;We&rsquo;re on a well and getting orange stains in the tubs. Had a water test done last spring.&quot;',
)
REVIEW = dict(quote=('Very responsive and explained about how my water treatment system works and also found and fixed a '
                     'leak that was in a hidden spot that could have caused damage.'),
              name='Chris H.', initials='CH', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Water treatment FAQ'
FAQ_HEADING = 'Water filtration questions, answered.'
FAQS = [
    ('How much does a water filtration or softener system cost?',
     'It depends on what your water needs, the size of your household and the type of equipment. A single sediment '
     'filter costs far less than a combined softener and iron treatment system. We give you a written quote after a '
     'free on-site visit, so you know the full price before work starts.'),
    ('Do I need a water test first?',
     'For well water, yes. A test from a state-certified lab shows hardness, iron, pH and other contaminants so the '
     'system can be matched to your water. If you already have recent results, have them handy for your visit.'),
    ('How long does installation take?',
     'Most single systems, such as a softener or whole-house filter, are installed in one visit. Combined systems or '
     'installs that need new drain or electrical connections can take longer. We will give you a timeline with your quote.'),
    ('Will a water softener lower my water pressure?',
     'A correctly sized system should not noticeably change your pressure. Pressure problems usually come from '
     'undersized equipment or clogged filters, which is why sizing and maintenance matter.'),
    ('How do I maintain my water treatment system?',
     'Softeners need salt added periodically, and filters need cartridges changed on a schedule that depends on your '
     'water and usage. We will show you what your system needs when we install it.'),
]

RELATED_HEADING = 'Other services that go with water treatment.'
RELATED = [
    ('well-systems-pressure-tanks', 'Pressure tanks, switches and low water pressure problems on private well systems.'),
    ('water-heater-installation', 'Water heaters replaced and installed, and protected from hard water and sediment.'),
    ('leak-frozen-pipe-repair', 'Pinhole leaks from acidic water and other leaking pipes found and repaired.'),
]

CTA = dict(h2='Ready for better water?',
           p='Get a free on-site visit and a clear, written quote for the right water treatment system. No obligation.')
