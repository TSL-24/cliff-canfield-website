SLUG = 'bathroom-remodels'
SERVICE_NAME = 'Bathroom Remodels'
KEYWORD = 'bathroom remodel'
SECONDARY_KEYWORDS = ['bathroom renovation', 'shower', 'vanity', 'tub']
TITLE = 'Bathroom Remodels in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Bathroom remodel and renovation plumbing in New Milford, Danbury and nearby CT towns. '
               'Licensed master plumber, clear written quotes.')
IMAGE = 'images/services/bathroom-remodels.jpg'

HERO = dict(
    eyebrow='Bathroom remodels · New Milford, CT',
    h1='Bathroom remodels in New Milford, CT',
    lead=('Planning a new bathroom? Get the plumbing done right from the start: new supply and drain lines, '
          'showers, tubs, vanities and fixtures, installed by a licensed master plumber who can also manage your '
          'complete remodel.'),
    cta='Get a free remodel quote',
    image=dict(src='images/services/bathroom-remodels.jpg', w=960, h=1200,
               alt='Bathroom remodel plumbing rough-in with PEX supply lines, PVC drains and a new tub in open wall framing',
               caption='Bathroom rough-in: new PEX supply lines, drains and tub ready for finish work'),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What a bathroom remodel involves',
         intro=('The plumbing is the part of a bathroom remodel you never see once the walls are closed, and the '
                'part that matters most. Getting it right means no leaks behind new tile, strong water pressure '
                'and drains that work for decades.'),
         paras=['Whether you are refreshing fixtures or gutting the room to the studs, a bathroom remodel '
                'typically includes:'],
         blocks=[dict(type='checklist', items=[
             'Planning the layout and fixture locations with you',
             'Removing old fixtures and outdated piping',
             'New water supply lines (often PEX) and shut-off valves',
             'Drain, waste and vent piping sized and sloped correctly',
             'Shower valves with scald protection and tub installation',
             'Vanity, sink, faucet and toilet installation',
             'Pressure-testing everything before walls are closed',
             'Final fixture setup, testing and cleanup'])]),
    dict(id='warning-signs', eyebrow='Common problems', h2='Signs it&rsquo;s time to renovate your bathroom',
         intro=('Many bathroom remodels start with a plumbing problem. These are the issues we see most often in '
                'older Connecticut homes:'),
         blocks=[dict(type='cards', cols=3, items=[
             ('Leaks and water damage', 'Soft floors, stained ceilings below or loose tiles usually mean water has been getting where it shouldn&rsquo;t.'),
             ('Old galvanized or failing pipes', 'Corroded steel or patched copper causes low pressure and rusty water, and is best replaced while walls are open.'),
             ('Shower temperature swings', 'Older valves without pressure balancing can scald when someone flushes. Modern valves fix that.'),
             ('Slow or noisy drains', 'Undersized or poorly vented drains gurgle and back up. A remodel is the time to correct them.'),
             ('Outdated or worn fixtures', 'Dripping faucets, cracked tubs and inefficient toilets waste water and money.'),
             ('A layout that doesn&rsquo;t work', 'Moving a toilet, adding a shower or a second sink means moving supply and drain lines.')])]),
    dict(id='options', eyebrow='Remodel options', h2='Choosing the right bathroom remodel for your home',
         intro='Every bathroom remodel is different. These are the most common project types we help with:',
         blocks=[dict(type='options', items=[
             ('Most flexible', 'Complete bathroom remodel', 'A full renovation from demolition to final fixtures, with Cliff able to act as the general contractor and coordinate the project.', ['One point of contact', 'Layout changes possible', 'Plumbing done right behind the walls']),
             ('Fast upgrade', 'Shower &amp; tub replacement', 'Replace a dated tub or shower, convert a tub to a walk-in shower, or upgrade to a modern valve.', ['Pressure-balanced or thermostatic valves', 'New drains and supply lines', 'Less disruption than a full remodel']),
             ('Fixture refresh', 'Vanity, sink &amp; faucet updates', 'New vanities, sinks, faucets and toilets installed on your existing plumbing, with repairs where needed.', ['Quick turnaround', 'Customer-supplied fixtures welcome', 'Good time to replace shut-off valves']),
             ('For contractors', 'Remodel plumbing only', 'Working with your own contractor or builder? We handle the rough-in and finish plumbing as part of your team.', ['Rough-in and finish plumbing', 'Coordinated scheduling', 'Code-compliant, inspection-ready work'])])]),
    dict(id='considerations', eyebrow='Project considerations', h2='What to plan for before your bathroom renovation',
         intro='A little planning up front keeps a bathroom remodel on budget and on schedule.',
         blocks=[dict(type='consider', items=[
             ('Layout changes', 'Keeping fixtures where they are costs less. Moving a toilet or shower means rerouting drains, which depends on your floor structure and access.'),
             ('Piping material', 'Remodels are the best time to replace old galvanized or failing copper. PEX is a common, durable choice for new supply lines.'),
             ('Fixture selection', 'Choose fixtures early. Valve bodies and drains are installed before walls close, and some fixtures need specific rough-in measurements.'),
             ('Water quality', 'Hard water and well water sediment are hard on new fixtures. Filtration or a softener protects your investment.'),
             ('Permits &amp; inspections', 'Most bathroom remodels involving new plumbing need a permit and inspection in Connecticut towns.'),
             ('Timeline', 'Plumbing happens in stages: rough-in before walls close, finish plumbing after tile and paint. Plan for both visits.')])]),
    dict(id='process', eyebrow='How it works', h2='Our bathroom remodel process',
         intro='You will know what is happening, what it costs and when each stage will be done.',
         blocks=[dict(type='steps', items=[
             ('Request a visit', 'Call us or send the form below with a few details about your bathroom.'),
             ('On-site walkthrough', 'We look at the space, the existing plumbing and your plans, and talk through options.'),
             ('Clear, written quote', 'You get a written quote before anything starts. No obligation and no surprises.'),
             ('Rough-in', 'New supply, drain and vent lines and valves are installed and pressure-tested before walls close.'),
             ('Finish &amp; walkthrough', 'Fixtures are installed, tested and adjusted, and the job site is cleaned up.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why homeowners choose us for their bathroom remodel',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Bathroom remodels in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we handle bathroom remodel plumbing for homeowners, contractors and builders across '
             'Western Connecticut, from Brookfield, Danbury and Newtown to Ridgefield, Southbury and Westport. '
             'Local means easier scheduling between remodel stages and a plumber who knows the older homes in your area.')

ESTIMATE = dict(
    heading='Get your bathroom remodel quote',
    lead=('Tell us about your bathroom and what you&rsquo;d like to change. We&rsquo;ll come out, look at the space '
          'and give you a clear price.'),
    options=[('Bathroom Remodel', 'Complete bathroom remodel'), ('Shower / Tub Replacement', 'Shower or tub replacement'),
             ('Fixture Updates', 'Vanity, sink &amp; fixture updates'), ('Remodel Plumbing (Contractor)', 'Plumbing for my contractor&rsquo;s project'),
             ('Other', 'Something else')],
    details_label='Tell us about your bathroom',
    placeholder='e.g. &quot;Full remodel of our upstairs bath. Want to swap the tub for a walk-in shower and add a double vanity.&quot;',
)
REVIEW = dict(quote=('We had a lot of fixtures to replace, each with a different challenge. I asked for quality products and '
                     'Cliff delivered with American Made Prier Plumbing and PEX piping. I explained the details and he was on '
                     'the job the next day. He gave me the estimate and it seemed fair. When he was done, everything looked '
                     'great and worked perfectly. Cliff is easy to work with and will deliver what you specified. When he was '
                     'done, he cleaned up the job sites completely. The final bill matched the estimate. No hidden charges. &hellip;'),
              name='Richard D.', initials='RD', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Bathroom remodel FAQ'
FAQ_HEADING = 'Bathroom remodel questions, answered.'
FAQS = [
    ('How much does a bathroom remodel cost?',
     'It depends on the size of the room, whether fixtures stay in place or move, the condition of the existing piping, '
     'and the fixtures and finishes you choose. Keeping the same layout costs far less than moving a toilet or shower. '
     'We give you a written, itemized quote after a free on-site visit, so you know the price before work starts.'),
    ('How long does a bathroom remodel take?',
     'A fixture refresh can often be done in a day or two. A full bathroom remodel takes longer because plumbing is '
     'done in stages, with rough-in before the walls close and finish plumbing after tile and paint. We will give you '
     'a realistic timeline with your quote.'),
    ('Can you manage my whole bathroom remodel, or just the plumbing?',
     'Both. Cliff can act as the general contractor for a complete bathroom remodel, or handle just the plumbing as '
     'part of your own contractor&rsquo;s team.'),
    ('Can I supply my own fixtures?',
     'Yes. Many customers choose their own faucets, vanities and toilets. Let us know what you have picked so we can '
     'confirm the rough-in measurements before the walls are closed.'),
    ('Do I need a permit for a bathroom remodel in Connecticut?',
     'Most remodels that add or change plumbing require a permit and inspection from your town&rsquo;s building '
     'department. We will tell you what your project needs during the on-site visit.'),
]

RELATED_HEADING = 'Other services for your bathroom project.'
RELATED = [
    ('fixture-installation-repair', 'Faucets, sinks, showers and tub fixtures installed or repaired, including fixtures you supply.'),
    ('toilet-repair-replacement', 'New toilets installed with a fresh seal, and running or leaking toilets repaired.'),
    ('water-filtration-treatment', 'Softeners and filtration that protect new fixtures from hard water and well sediment.'),
]

CTA = dict(h2='Ready to plan your new bathroom?',
           p='Get a free on-site visit and a clear, written quote for your bathroom remodel. No obligation.')
