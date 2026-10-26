SLUG = 'fixture-installation-repair'
SERVICE_NAME = 'Fixture Installation & Repair'
KEYWORD = 'fixture installation'
SECONDARY_KEYWORDS = ['faucet', 'sink', 'shower valve', 'faucet replacement']
TITLE = 'Fixture Installation in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Faucet, sink, shower and toilet fixture installation and repair in New Milford, Danbury and nearby '
               'CT towns. Your fixtures or ours.')
IMAGE = None

HERO = dict(
    eyebrow='Fixtures · New Milford, CT',
    h1='Plumbing fixture installation &amp; repair in New Milford, CT',
    lead=('New faucet, sink, shower valve or toilet? Get it installed right, with new supply lines and shut-off '
          'valves where needed, by a licensed master plumber. Your fixtures or ones we source for you.'),
    cta='Get a free fixture quote',
    panel=dict(title='Fixtures we install &amp; repair', items=[
        'Kitchen and bathroom faucets',
        'Sinks and vanities',
        'Shower and tub valves',
        'Tubs and shower bases',
        'Toilets',
        'Outdoor spigots and hose bibs']),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What fixture installation involves',
         intro=('A new faucet or sink looks simple, but a proper fixture installation is what keeps it from leaking '
                'into your cabinet or wall a year from now.'),
         paras=['Every fixture installation or repair includes:'],
         blocks=[dict(type='checklist', items=[
             'Checking the fixture fits your existing plumbing',
             'Removing the old fixture carefully',
             'New supply lines where needed',
             'Replacing worn or stuck shut-off valves',
             'Proper sealing, mounting and drain connections',
             'Setting temperature limits on shower valves',
             'Testing for leaks under pressure',
             'Cleaning up when we&rsquo;re done'])]),
    dict(id='warning-signs', eyebrow='Common problems', h2='Signs a fixture needs repair or replacement',
         intro='These are the fixture problems we fix most often:',
         blocks=[dict(type='cards', cols=3, items=[
             ('Dripping faucets', 'A constant drip wastes water and usually means a worn cartridge or washer.'),
             ('Leaks under the sink', 'Water in the cabinet often comes from supply lines, the faucet base or the drain connection.'),
             ('Low flow at one fixture', 'Clogged aerators, cartridges or failing supply lines can choke flow at a single faucet.'),
             ('Shower temperature swings', 'Older valves can run hot or cold when someone uses water elsewhere. Modern valves prevent it.'),
             ('Loose or wobbly fixtures', 'Faucets and toilets that move can damage connections and lead to hidden leaks.'),
             ('Worn, dated fixtures', 'Corroded finishes, cracked sinks and old faucets are often worth replacing rather than repairing.')])]),
    dict(id='options', eyebrow='Installation options', h2='Fixture installation and repair options',
         intro='Whatever you&rsquo;re updating, these are the most common jobs:',
         blocks=[dict(type='options', items=[
             ('Most common', 'Faucet installation &amp; repair', 'Faucet repair or faucet replacement for kitchens, bathrooms and bars, including pull-down and touchless models.', ['New supply lines', 'Leak-free mounting', 'Works with your sink']),
             ('Kitchen &amp; bath', 'Sinks &amp; vanities', 'Drop-in, undermount and vessel sinks and vanities installed and connected.', ['Drain and trap connections', 'Shut-off valves', 'Clean, sealed install']),
             ('Safety upgrade', 'Shower &amp; tub valves', 'New shower and tub valves with scald protection, plus trim and showerhead updates.', ['Steady water temperature', 'Pressure-balanced valves', 'Updated trim']),
             ('Your choice', 'Customer-supplied fixtures', 'Already picked out your fixtures? We will install the faucet, sink or toilet you bought.', ['We confirm the fit first', 'Professional install', 'No pressure to buy from us'])])]),
    dict(id='considerations', eyebrow='Project considerations', h2='What to consider before replacing a fixture',
         intro='A few details make your new fixture fit right and last.',
         blocks=[dict(type='consider', items=[
             ('Fit &amp; holes', 'Faucets come in single-hole and multi-hole designs. Matching your sink or countertop avoids surprises.'),
             ('Valve compatibility', 'Shower trim often only fits its own brand of valve. Changing brands may mean replacing the valve in the wall.'),
             ('Shut-off valves', 'Old shut-offs often leak or won&rsquo;t close. Replacing them during a fixture swap is quick and smart.'),
             ('Water quality', 'Hard water and well sediment wear out cartridges and finishes. Filtration protects new fixtures.'),
             ('Quality', 'Better-made fixtures with replaceable cartridges are easier and cheaper to repair later.'),
             ('Access', 'Clearing out the cabinet or area under the fixture helps the installation go faster.')])]),
    dict(id='process', eyebrow='How it works', h2='Our fixture installation process',
         intro='Simple, clean and done right the first time.',
         blocks=[dict(type='steps', items=[
             ('Request a visit', 'Tell us what you are replacing and whether you already have the new fixture.'),
             ('Confirm the fit', 'We check your plumbing and confirm the fixture will fit before installing.'),
             ('Clear price', 'You get a clear price before any work begins.'),
             ('Install &amp; test', 'We install the fixture, test it for leaks and clean up when we&rsquo;re done.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why homeowners choose us for fixture installation',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Fixture installation in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we install and repair faucets, sinks, showers and toilets for homeowners across '
             'Western Connecticut, from Brookfield, Danbury and Newtown to Ridgefield, Southbury and Westport. Local '
             'means easier scheduling and a plumber who knows the homes and water in your area.')

ESTIMATE = dict(
    heading='Get your fixture quote',
    lead=('Tell us which fixtures you&rsquo;re replacing or repairing, and whether you already have the new ones. '
          'We&rsquo;ll give you a clear price.'),
    options=[('Fixture Installation', 'Faucet installation or repair'), ('Sink / Vanity', 'Sink or vanity'),
             ('Shower / Tub Valve', 'Shower or tub valve'), ('Toilet', 'Toilet'), ('Multiple Fixtures', 'Several fixtures'),
             ('Other', 'Something else')],
    details_label='Tell us about your fixtures',
    placeholder='e.g. &quot;Replacing two bathroom faucets and a kitchen faucet. Already bought them.&quot;',
)
REVIEW = dict(quote='Fixed our leaking faucet by replacing it with hardware we purchased ourselves. Immediate response and great customer service.',
              name='Stephen K.', initials='SK', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Fixture FAQ'
FAQ_HEADING = 'Fixture installation questions, answered.'
FAQS = [
    ('How much does fixture installation cost?',
     'It depends on the fixture, the condition of the plumbing behind it and whether valves or supply lines need '
     'replacing. Swapping a faucet on good plumbing costs far less than replacing a shower valve inside the wall. '
     'You get a clear price before any work starts.'),
    ('Can you install a faucet or fixture I bought myself?',
     'Yes. We are happy to install fixtures you supply. Send us the model or a photo of the box so we can confirm it '
     'fits your sink, countertop or valve.'),
    ('Should I repair or replace my faucet?',
     'If the faucet is in good shape, a new cartridge or washer often fixes drips. If it is corroded, discontinued or '
     'leaking at the body, replacement is usually the better value. We will give you both options.'),
    ('How long does it take to install a new faucet or sink?',
     'Most faucet swaps are done in a single visit. Sinks, vanities and shower valves take longer, especially when '
     'plumbing needs to be adjusted. We will give you a timeline with your quote.'),
    ('Can you install several fixtures in one visit?',
     'Yes. Replacing several fixtures at once is often more efficient. Let us know everything on your list so we can '
     'plan the time and parts.'),
]

RELATED_HEADING = 'Other services that go with new fixtures.'
RELATED = [
    ('bathroom-remodels', 'Complete bathroom remodels, or the plumbing for your contractor&rsquo;s project.'),
    ('toilet-repair-replacement', 'Running, leaking and wobbly toilets repaired, or replaced with a new, efficient model.'),
    ('water-filtration-treatment', 'Softeners and filtration that protect new fixtures from hard water and sediment.'),
]

CTA = dict(h2='Ready for new fixtures?',
           p='Get a clear price for your faucet, sink, shower or toilet installation. Your fixtures or ours.')
