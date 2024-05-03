import { LuzmoDashboardComponent, LuzmoDashboard } from '@luzmo/react-embed'
import { useRef } from 'react'

export default function DashboardLayout({
        children,
    }: {
        children: React.ReactNode
    }){
        return (
            <section>
                {
                    // Insert shared UI of header
                    <nav></nav>
                    {children}
                }
            </section>
        )
}



function LuzmoWrapper() {
    const ref = useRef<LuzmoDashboard>?null;
    return (
        <div className ="App">
            <button
                onClick={async (e) => console.log(await ref.current.exportDashboard())}
            >
                Export Dashboard
            </button>
            <LuzmoDashboardComponent 
                ref={ref}
                authKey=""
                authToken=""
                dashboardSlug="test"
                switchScreenModeOnResize={false}
                loaderSpinnerColor="rgb(0, 81, 128)"
                loaderSpinnerBackground='rgb(236 248 255)'
                itemsRendered={(e) => console.log('itemsRendered', e)}>
            </LuzmoDashboardComponent>
        </div>
    );
}